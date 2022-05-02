import os, requests, threading

ss = [200, 201, 204]

class XyloLmao:
    def TokenChecker():
        if os.path.exists("ValidTokens.txt"):
            os.remove("ValidTokens.txt")
        else:
            with open("ValidTokens.txt", "a")as f:
                pass
                
        if not os.path.exists("Tokens.txt"):
            with open("Tokens.txt", "a")as f:
                pass
                
        with open("Tokens.txt", "r")as g:
            valid = 0
            invalid = 0
            tokens = []
            os.system(f"title Valid Tokens: {valid} ~ Invalid Tokens: {invalid}")
            for token in g:
                if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token}).status_code in ss:    
                    valid += 1
                    tokens.append(token)
                else:
                    invalid += 1
                    
        with open("ValidTokens.txt", "a")as l:
            for t in tokens:
                l.write(t + "\n")
                    
if __name__ == "__main__":
    t1 = []
    t = threading.Thread(target=XyloLmao.TokenChecker)
    t.start()
    t1.append(t)
    for thread in t1:
        thread.join()
    