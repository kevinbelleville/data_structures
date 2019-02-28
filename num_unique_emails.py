def numUniqueEmails(emails):
        # strip out periods
        # remove everything after the + until the @
        # break the email apart from the @ symbol
        unique_emails = []
        for address in emails:
            name, domain = address.split("@")
            for letter, index in enumerate(name):
                if letter == ".":
                    first, second = name.split(".")
                    name = first+second
                if letter == "+":
                    name = name[:i]
            unique_emails.append(name+"@"+domain)
        print(unique_emails)
        return len(unique_emails)