from concurrent.futures import ThreadPoolExecutor
import os
import re 

def word_count(path):
    
    kv = {}
    with open(path,mode="r",encoding="latin-1") as fp:
        
        for line in fp:
            words = re.sub(r'[^a-zA-Z0-9 ]', '', line)
            # print(wor)
            for w in words.lower().split(" "):
                if w in kv:
                    kv[w] += 1
                else:
                    kv[w] = 1
    return kv    

if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=6) as texec:        
        futures = [texec.submit(word_count, f"{os.getcwd()}/files/{fpath}") for fpath in os.listdir(path="./files")]

        global_kv = {}
        for f in futures:
            for k,v in  f.result().items():
                if k in global_kv:
                    global_kv[k] += v
                else:
                    global_kv[k] = v 
        
        print(len(global_kv))
            

   