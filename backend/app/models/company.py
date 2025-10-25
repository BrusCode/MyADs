"""
Company model
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Company(Base):
    """Company model"""
    __tablename__ = "companies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    legal_name = Column(String(255), nullable=True)
    document = Column(String(20), unique=True, nullable=True, index=True)  # CNPJ/CPF
    
    # Contact
    email = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)
    website = Column(String(500), nullable=True)
    
    # Address
    address = Column(String(500), nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(50), nullable=True)
    country = Column(String(50), default="Brasil", nullable=False)
    postal_code = Column(String(20), nullable=True)
    
    # Settings
    timezone = Column(String(50), default="America/Sao_Paulo", nullable=False)
    currency = Column(String(3), default="BRL", nullable=False)
    language = Column(String(10), default="pt-BR", nullable=False)
    
    # Branding
    logo_url = Column(String(500), nullable=True)
    primary_color = Column(String(7), default="#3B82F6", nullable=False)  # Hex color
    secondary_color = Column(String(7), default="#10B981", nullable=False)
    
    # Status
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Notes
    notes = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    users = relationship("CompanyUser", back_populates="company", cascade="all, delete-orphan")
    ad_accounts = relationship("AdAccount", back_populates="company", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Company {self.name}>"


class CompanyUser(Base):
    """Company-User relationship (many-to-many with additional fields)"""
    __tablename__ = "company_users"
    
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Role within this company
    role = Column(String(50), default="viewer", nullable=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="users")
    user = relationship("User", back_populates="companies")
    
    def __repr__(self):
        return f"<CompanyUser company_id={self.company_id} user_id={self.user_id} role={self.role}>"

