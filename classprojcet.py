def google_map_project(**info): 
 
 print("The country is " + info ["country"])
 print("The budget is " + info["budget"])
 print("The staff is "  + info ["staff"]) 
 
google_map_project (budget ="10000", country = "USA", staff= "100")






def print_triangle(n):
    for i in range(1, n+1):
        print('*' * i)

print_triangle(5)