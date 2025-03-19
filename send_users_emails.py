import json
import random
import time
from utils.misc.send_email2 import send_email2
import argparse

# Define available universities
universities = [
    'stanford', 
    'harvard', 
    'yale', 
    'dartmouth', 
    'duke', 
    'nyuad', 
    'princeton', 
    'uchicago'
]

# Load users from the JSON file
with open('users.json', 'r') as f:
    users = json.load(f)

# Function to send email with delay
def send_with_delay(user, delay_range=(5, 15), test_mode=False):
    """
    Send email to a user with random university and add delay
    
    Args:
        user: Dictionary containing email and name
        delay_range: Tuple of (min_seconds, max_seconds) to delay between emails
        test_mode: If True, only print what would be sent without actually sending
    """
    # Choose random university
    university = random.choice(universities)
    
    # Extract user info
    email = user['email']
    name = user['name']
    
    # Set the decision to always be acceptance
    decision = 'acceptance'
    
    # Print info about the email being sent
    print(f"Sending {decision} email from {university.upper()} to {name} ({email})...")
    
    if test_mode:
        print(f"TEST MODE: Would send email from {university.title()} to {email} with name {name}")
        return True
    
    try:
        # Send the email
        send_email2(
            sender_name=university.title(), 
            receiver_email=email, 
            first_name=name, 
            decision=decision, 
            university=university
        )
        print(f"✓ Email sent successfully to {email}")
        return True
    except Exception as e:
        print(f"✗ Failed to send email to {email}: {str(e)}")
        return False
    
    finally:
        # Random delay between emails to avoid rate limiting
        if not test_mode:
            delay = random.uniform(delay_range[0], delay_range[1])
            print(f"Waiting {delay:.1f} seconds before sending next email...\n")
            time.sleep(delay)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Send acceptance emails to users')
    parser.add_argument('--test', action='store_true', help='Run in test mode without sending emails')
    parser.add_argument('--limit', type=int, default=None, help='Limit the number of emails to send')
    parser.add_argument('--validate', action='store_true', help='Just test one email to validate credentials')
    args = parser.parse_args()
    
    if args.validate:
        print("Running in credential validation mode - will attempt to send a single test email")
        # Use your own test email here or the first user in the list
        test_user = {'email': users[0]['email'], 'name': users[0]['name']}
        result = send_with_delay(test_user, test_mode=args.test)
        if result:
            print("Credentials appear to be valid!")
        else:
            print("Credential validation failed. Please check your config settings.")
        return
    
    # Limit users if specified
    if args.limit:
        users_to_process = users[:args.limit]
        print(f"Limited to sending first {args.limit} emails (out of {len(users)} total)")
    else:
        users_to_process = users
    
    total_users = len(users_to_process)
    
    if args.test:
        print(f"TEST MODE: Will simulate sending emails to {total_users} users without actually sending")
    else:
        print(f"Starting to send emails to {total_users} users...")
    
    # Ask for confirmation before starting
    if not args.test:  # Don't need confirmation in test mode
        confirm = input(f"This will send acceptance emails to {total_users} users. Are you sure? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation cancelled.")
            return
    
    # Track progress
    for i, user in enumerate(users_to_process, 1):
        print(f"Processing {i}/{total_users}: ", end="")
        success = send_with_delay(user, test_mode=args.test)
        
        # If first email fails and not in test mode, ask if we should continue
        if i == 1 and not success and not args.test:
            continue_after_error = input("First email failed. Continue with remaining emails? (y/n): ")
            if continue_after_error.lower() != 'y':
                print("Operation cancelled.")
                return
        yield
        # Every 10 emails, wait a bit longer to be safe
        if i % 10 == 0 and not args.test:
            longer_delay = random.uniform(20, 30)
            print(f"Completed {i}/{total_users} emails. Taking a longer break ({longer_delay:.1f}s)...")
            time.sleep(longer_delay)
    
    print(f"{'TEST MODE: ' if args.test else ''}Completed sending emails to all {total_users} users!")

if __name__ == "__main__":
    main() 