user_name = input("Hello, Human. What's your name?  ")

print(user_name)

while True:
    original_user_response = input("My name is cas. What kind of movie would you like to hear about?   ")
    user_response = original_user_response.lower()
    print(user_response)
    
    if "romcom" in user_response:
            print("the newest movie in 2021 is Coming 2 America that is rated pg-13")
            break
                
    if user_response == "romcom":
            print("the newest movie in 2021 is Coming 2 America that is rated pg-13") 
            break
        
    if "horror" in user_response:
            print("the newest movie in 2021 is wrong turn that is rated R")
            break
                
    if user_response == "horror":
            print("the newest movie in 2021 is wrong turn") 
            break
    
    if "comedy" in user_response:
            print("the newest movie in 2021 is Tom and jerry that is rated pg")
            break
    if user_response == "comedy":
        print("the newest movie in 2021 is Tom and jerry that is rated pg") 
        break
    
    if "quit" in user_response:
        print("is exactly 'quit'")
        break

    if user_response == "quit":
        print("is exactly 'quit'")
        break


print("interesting.... \ngood bye")
    
#outside while loop
#print("good bye")