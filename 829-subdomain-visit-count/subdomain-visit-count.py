class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        if cpdomains is None:
            return []
        
        domainStrings = {}
        for domain in cpdomains:
            count,address = domain.split(" ")
            counter = 0
            subdomains = address.split(".")
            for subdomain in subdomains:
                #print(subdomain)
                if counter != len(subdomains)-1:
                    subdomain = ".".join(subdomains[counter:])
                if subdomain not in domainStrings:
                    domainStrings[subdomain] = int(count)
                else:
                    domainStrings[subdomain] += int(count)
                counter+=1
                
                
        finalList = []
        for key in domainStrings:
            string = "{} {}".format(domainStrings[key], key)
            finalList.append(string)

        

        return finalList