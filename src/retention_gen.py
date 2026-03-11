import sys

def generate_retention_message(customer_data):
    """
    Simulates an LLM-based system using Prompt Engineering 
    to create personalized retention offers for high-risk customers.
    """
    
    # 1. Extracting Customer Data
    tenure = customer_data.get('tenure', 0)
    contract = customer_data.get('contract', 'Month-to-month')
    internet = customer_data.get('internet_service', 'Fiber optic')
    
    # 2. PROMPT ENGINEERING 
    # This is the instruction we 'feed' to the LLM to control its behavior.
    prompt = f"""
    SYSTEM: You are a professional customer retention specialist for a Telecom company.
    INPUT: The customer has a tenure of {tenure} months, is on a {contract} contract, and uses {internet} service.
    TASK: Based on the Churn prediction, generate a highly personalized and friendly loyalty incentive message.
    """

    # 3. LLM Simulation (Mock Response)
    # Logic: Customers with higher tenure (> 24 months) get a bigger reward.
    loyalty_bonus = "a 25% discount and a free high-speed upgrade" if tenure > 24 else "a 15% discount"
    
    retention_message = (
        f"Dear Valued Customer, we truly appreciate your loyalty over the past {tenure} months. "
        f"As a long-term {internet} user, you are eligible for a special reward. "
        f"We are offering you {loyalty_bonus} on your next {contract} bill! "
        f"Reply 'STAY' to activate this offer instantly."
    )

    # 4. Displaying the Output in Terminal for the Video Demo
    print("\n" + "="*65)
    print("🤖 LLM PROMPT (The 'Prompt Engineering' Part):")
    print(prompt.strip())
    print("-" * 65)
    print("✨ GENERATED RETENTION MESSAGE (LLM Output):")
    print(f"\"{retention_message}\"")
    print("="*65 + "\n")

if __name__ == "__main__":
    # Sample High-Risk Customer for the Presentation
    high_risk_customer = {
        'tenure': 36, 
        'contract': 'One year', 
        'internet_service': 'Fiber optic'
    }
    
    generate_retention_message(high_risk_customer)
