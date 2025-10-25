"""
Metric model
"""
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Metric(Base):
    """Metric model - stores daily metrics for campaigns"""
    __tablename__ = "metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    ad_account_id = Column(Integer, ForeignKey("ad_accounts.id", ondelete="CASCADE"), nullable=False, index=True)
    campaign_id = Column(String(255), nullable=False, index=True)
    
    # Date
    date = Column(Date, nullable=False, index=True)
    
    # Reach metrics
    impressions = Column(Integer, default=0, nullable=False)
    reach = Column(Integer, default=0, nullable=True)
    frequency = Column(Float, default=0.0, nullable=True)
    
    # Engagement metrics
    clicks = Column(Integer, default=0, nullable=False)
    ctr = Column(Float, default=0.0, nullable=False)  # Click-through rate
    interactions = Column(Integer, default=0, nullable=True)
    
    # Conversion metrics
    conversions = Column(Integer, default=0, nullable=False)
    conversion_rate = Column(Float, default=0.0, nullable=False)
    conversion_value = Column(Float, default=0.0, nullable=False)
    
    # Cost metrics
    cost = Column(Float, default=0.0, nullable=False)
    cpc = Column(Float, default=0.0, nullable=False)  # Cost per click
    cpm = Column(Float, default=0.0, nullable=False)  # Cost per mille (thousand impressions)
    cpa = Column(Float, default=0.0, nullable=False)  # Cost per acquisition
    
    # Return metrics
    roas = Column(Float, default=0.0, nullable=False)  # Return on ad spend
    revenue = Column(Float, default=0.0, nullable=False)
    
    # Video metrics (for video campaigns)
    video_views = Column(Integer, default=0, nullable=True)
    video_view_rate = Column(Float, default=0.0, nullable=True)
    
    # Social metrics (for Meta Ads)
    likes = Column(Integer, default=0, nullable=True)
    comments = Column(Integer, default=0, nullable=True)
    shares = Column(Integer, default=0, nullable=True)
    saves = Column(Integer, default=0, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    ad_account = relationship("AdAccount", back_populates="metrics")
    
    # Composite index for efficient queries
    __table_args__ = (
        Index('idx_ad_account_date', 'ad_account_id', 'date'),
        Index('idx_campaign_date', 'campaign_id', 'date'),
    )
    
    def __repr__(self):
        return f"<Metric campaign={self.campaign_id} date={self.date}>"
    
    def to_dict(self):
        """Convert metric to dictionary"""
        return {
            "id": self.id,
            "ad_account_id": self.ad_account_id,
            "campaign_id": self.campaign_id,
            "date": self.date.isoformat() if self.date else None,
            "impressions": self.impressions,
            "reach": self.reach,
            "frequency": self.frequency,
            "clicks": self.clicks,
            "ctr": self.ctr,
            "interactions": self.interactions,
            "conversions": self.conversions,
            "conversion_rate": self.conversion_rate,
            "conversion_value": self.conversion_value,
            "cost": self.cost,
            "cpc": self.cpc,
            "cpm": self.cpm,
            "cpa": self.cpa,
            "roas": self.roas,
            "revenue": self.revenue,
            "video_views": self.video_views,
            "video_view_rate": self.video_view_rate,
            "likes": self.likes,
            "comments": self.comments,
            "shares": self.shares,
            "saves": self.saves,
        }

