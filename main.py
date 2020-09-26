import dns.resolver

ids = [
    "A",
    "NS",
    "CNAME",
    "SOA",
    "MX",
    "TXT",
    "AAAA",
]

def resolve(domain: str):
    result = []
    for record in ids:
        try:
            answers = dns.resolver.resolve(domain, record)
            data = [{"record": record, "value": rdata.to_text()} for rdata in answers]
            for item in data:
                result.append(item)
        except Exception as e:
            print(e)
    return result

print(resolve('jolvera.dev'))