# app/models.py

class CustomerData:
    def __init__(self, **kwargs):
        self.customer_id = kwargs.get('customer_id')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.email = kwargs.get('email')
        self.phone_number = kwargs.get('phone_number')
        self.date_of_birth = kwargs.get('date_of_birth')
        self.gender = kwargs.get('gender')
        self.address_line1 = kwargs.get('address_line1')
        self.address_line2 = kwargs.get('address_line2')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.postal_code = kwargs.get('postal_code')
        self.country = kwargs.get('country')
        self.join_date = kwargs.get('join_date')
        self.last_purchase_date = kwargs.get('last_purchase_date')
        self.total_spend = kwargs.get('total_spend')
        self.average_order_value = kwargs.get('average_order_value')
        self.order_count = kwargs.get('order_count')
        self.is_loyalty_member = kwargs.get('is_loyalty_member')
        self.loyalty_points = kwargs.get('loyalty_points')
        self.preferred_store = kwargs.get('preferred_store')
        self.communication_preference = kwargs.get('communication_preference')
        self.subscription_status = kwargs.get('subscription_status')
        self.has_purchased = kwargs.get('has_purchased')
        self.opt_in_email = kwargs.get('opt_in_email')
        self.opt_in_sms = kwargs.get('opt_in_sms')
        self.customer_segment = kwargs.get('customer_segment')
        self.marketing_source = kwargs.get('marketing_source')
        self.last_login_date = kwargs.get('last_login_date')
        self.preferred_language = kwargs.get('preferred_language')
        self.referral_code = kwargs.get('referral_code')
        self.referral_count = kwargs.get('referral_count')
        self.feedback_score = kwargs.get('feedback_score')
        self.churn_risk = kwargs.get('churn_risk')
        self.account_status = kwargs.get('account_status')
        self.customer_notes = kwargs.get('customer_notes')
        self.occupation = kwargs.get('occupation')
        self.industry = kwargs.get('industry')
        self.income_level = kwargs.get('income_level')
        self.education_level = kwargs.get('education_level')
        self.marital_status = kwargs.get('marital_status')
        self.children_count = kwargs.get('children_count')
        self.household_size = kwargs.get('household_size')
        self.annual_spend = kwargs.get('annual_spend')
        self.favorite_product = kwargs.get('favorite_product')
        self.preferred_payment_method = kwargs.get('preferred_payment_method')
        self.account_manager = kwargs.get('account_manager')
        self.social_media_handle = kwargs.get('social_media_handle')
        self.customer_satisfaction_score = kwargs.get('customer_satisfaction_score')
        self.preferred_contact_time = kwargs.get('preferred_contact_time')

        # Add any additional properties dynamically
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def get_fields(cls):
        return [attr for attr in cls.__init__.__code__.co_varnames if attr != 'self' and not attr.startswith('_')]
