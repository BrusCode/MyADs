"""
Ad Account model
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.database import Base


class AdPlatform(str, enum.Enum):
    """Ad platform enum"""
    GOOGLE_ADS = "google_ads"
    META_ADS = "meta_ads"


class AdAccountStatus(str, enum.Enum):
    """Ad account status enum"""
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    ERROR = "error"
    TOKEN_EXPIRED = "token_expired"


class AdAccount(Base):
    """Ad Account model"""
    __tablename__ = "ad_accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Platform
    platform = Column(SQLEnum(AdPlatform), nullable=False, index=True)
    
    # Account info
    account_id = Column(String(255), nullable=False, index=True)  # Platform-specific account ID
    account_name = Column(String(255), nullable=False)
    currency = Column(String(3), nullable=True)
    timezone = Column(String(50), nullable=True)
    
    # OAuth tokens (encrypted in production)
    access_token = Column(Text, nullable=False)
    refresh_token = Column(Text, nullable=True)
    token_expires_at = Column(DateTime(timezone=True), nullable=True)
    
    # Status
    status = Column(SQLEnum(AdAccountStatus), default=AdAccountStatus.CONNECTED, nullable=False)
    last_sync_at = Column(DateTime(timezone=True), nullable=True)
    last_error = Column(Text, nullable=True)
    
    # Settings
    is_active = Column(Boolean, default=True, nullable=False)
    auto_sync = Column(Boolean, default=True, nullable=False)
    sync_frequency_minutes = Column(Integer, default=60, nullable=False)  # Sync every hour
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="ad_accounts")
    campaigns = relationship("Campaign", back_populates="ad_account", cascade="all, delete-orphan")
    metrics = relationship("Metric", back_populates="ad_account", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<AdAccount {self.platform.value} - {self.account_name}>"
    
    @property
    def is_google_ads(self) -> bool:
        """Check if account is Google Ads"""
        return self.platform == AdPlatform.GOOGLE_ADS
    
    @property
    def is_meta_ads(self) -> bool:
        """Check if account is Meta Ads"""
        return self.platform == AdPlatform.META_ADS
    
    @property
    def needs_token_refresh(self) -> bool:
        """Check if token needs refresh"""
        if not self.token_expires_at:
            return False
        from datetime import datetime, timedelta
        # Refresh if expires in less than 1 day
        return datetime.utcnow() + timedelta(days=1) > self.token_expires_at


class Campaign(Base):
    """Campaign model"""
    __tablename__ = "campaigns"
    
    id = Column(Integer, primary_key=True, index=True)
    ad_account_id = Column(Integer, ForeignKey("ad_accounts.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Campaign info
    campaign_id = Column(String(255), nullable=False, index=True)  # Platform-specific campaign ID
    campaign_name = Column(String(255), nullable=False, index=True)
    campaign_status = Column(String(50), nullable=True)
    
    # Budget
    daily_budget = Column(String(50), nullable=True)
    lifetime_budget = Column(String(50), nullable=True)
    
    # Dates
    start_date = Column(DateTime(timezone=True), nullable=True)
    end_date = Column(DateTime(timezone=True), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    ad_account = relationship("AdAccount", back_populates="campaigns")
    
    def __repr__(self):
        return f"<Campaign {self.campaign_name}>"

