def main():
    users_emails = {}
    email_until = input('Email:')
    while email_until != ' ':
        name = extract_name_from_email(email_until)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ('y', ''):
            name = input("Name: ").strip().title()
        users_emails[email_until] = name
        email_until = input('Email:')
    print("\nStored emails and names:")
    for email, name in users_emails.items():
        print(f"{name} ({email})")


def extract_name_from_email(email_until):
    local_part = email_until.split('@')[0]
    parts = ''.join(c if c.isalpha() else ' ' for c in local_part).split()
    name = ' '.join(part.title() for part in parts)
    return name



main()