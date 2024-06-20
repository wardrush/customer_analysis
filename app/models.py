# frontend/models.py
from dataclasses import dataclass, field, fields
from typing import Optional, Any, Dict, List
from datetime import datetime

@dataclass
class BaseModel:
    @classmethod
    def get_fields(cls) -> List[str]:
        return [field.name for field in fields(cls)]
@dataclass
class Contact(BaseModel):
    contact_id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    properties: Dict[str, Any] = field(default_factory=dict)
    company_or_companies: List['Company'] = field(default_factory=list)
    deals_or_deals: List['Deal'] = field(default_factory=list)
    tickets: List['Ticket'] = field(default_factory=list)

@dataclass
class CustomerModel(Contact):
    customer_id: str = None
    first_name: str = None
    last_name: str = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    gender: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    join_date: Optional[datetime] = None
    last_purchase_date: Optional[datetime] = None
    total_spend: Optional[float] = None
    average_order_value: Optional[float] = None
    order_count: Optional[int] = None
    is_loyalty_member: Optional[bool] = None
    loyalty_points: Optional[int] = None
    preferred_store: Optional[str] = None
    communication_preference: Optional[str] = None
    subscription_status: Optional[str] = None
    has_purchased: Optional[bool] = None
    opt_in_email: Optional[bool] = None
    opt_in_sms: Optional[bool] = None
    customer_segment: Optional[str] = None
    marketing_source: Optional[str] = None
    last_login_date: Optional[datetime] = None
    preferred_language: Optional[str] = None
    referral_code: Optional[str] = None
    referral_count: Optional[int] = None
    feedback_score: Optional[float] = None
    churn_risk: Optional[str] = None
    account_status: Optional[str] = None
    customer_notes: Optional[str] = None
    occupation: Optional[str] = None
    industry: Optional[str] = None
    income_level: Optional[str] = None
    education_level: Optional[str] = None
    marital_status: Optional[str] = None
    children_count: Optional[int] = None
    household_size: Optional[int] = None
    annual_spend: Optional[float] = None
    favorite_product: Optional[str] = None
    preferred_payment_method: Optional[str] = None
    account_manager: Optional[str] = None
    social_media_handle: Optional[str] = None
    customer_satisfaction_score: Optional[float] = None
    preferred_contact_time: Optional[str] = None
    extra_fields: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self, **kwargs):
        # Ensure datetime fields are properly initialized if provided as strings or other types
        if isinstance(self.date_of_birth, str):
            self.date_of_birth = datetime.fromisoformat(self.date_of_birth)
        if isinstance(self.join_date, str):
            self.join_date = datetime.fromisoformat(self.join_date)
        if isinstance(self.last_purchase_date, str):
            self.last_purchase_date = datetime.fromisoformat(self.last_purchase_date)
        if isinstance(self.last_login_date, str):
            self.last_login_date = datetime.fromisoformat(self.last_login_date)

        # Handle extra kwargs and add them to extra_fields
        for key, value in kwargs.items():
            if not hasattr(self, key):
                self.extra_fields[key] = value

@dataclass
class Company(BaseModel):
    company_id: str
    name: Optional[str] = None
    domain: Optional[str] = None
    industry: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    properties: Dict[str, Any] = field(default_factory=dict)
    contacts: List[Contact] = field(default_factory=list)
    deals: List['Deal'] = field(default_factory=list)
    tickets: List['Ticket'] = field(default_factory=list)

@dataclass
class Deal(BaseModel):
    deal_id: str
    name: Optional[str] = None
    amount: Optional[float] = None
    stage: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    properties: Dict[str, Any] = field(default_factory=dict)
    contacts: List[Contact] = field(default_factory=list)
    companies: List[Company] = field(default_factory=list)
    tickets: List['Ticket'] = field(default_factory=list)

@dataclass
class Ticket(BaseModel):
    ticket_id: str
    subject: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    properties: Dict[str, Any] = field(default_factory=dict)
    contacts: List[Contact] = field(default_factory=list)
    companies: List[Company] = field(default_factory=list)
    deals: List[Deal] = field(default_factory=list)

@dataclass
class Activity(BaseModel):
    activity_id: str
    type: str
    timestamp: datetime = field(default_factory=datetime.now)
    details: Dict[str, Any] = field(default_factory=dict)
    contacts: List[Contact] = field(default_factory=list)
    companies: List[Company] = field(default_factory=list)
    deals: List[Deal] = field(default_factory=list)
    tickets: List[Ticket] = field(default_factory=list)

@dataclass
class Product(BaseModel):
    product_id: str
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    properties: Dict[str, Any] = field(default_factory=dict)
    deals: List[Deal] = field(default_factory=list)

# Class method to get fields of the dataclass


# Example usage
if __name__ == "__main__":
    print("DataClass Field Names:")
    contact_field_names = Contact.get_fields()
    print("Contact: ", contact_field_names)
    customer_field_names = CustomerModel.get_fields()
    print("CustomerModel (Inherits Contact): ", customer_field_names)
    company_field_names = Company.get_fields()
    print("Company: ", company_field_names)
    activity_field_names = Activity.get_fields()
    print("Activity: ", activity_field_names)
    deal_field_names = Deal.get_fields()
    print("Deal: ", deal_field_names)
    ticket_field_names = Ticket.get_fields()
    print("Ticket: ", ticket_field_names)
    product_field_names = Product.get_fields()
    print("Product: ", product_field_names)
