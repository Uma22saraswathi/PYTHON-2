#Print the value of the key ‘history’ from a given dictionary
sample_dict={
    "class":{
        "student":{
          "name":"uma",  
         "marks":{
            "physics":70,
            "history":80
         } 
        }
    }
}
print(sample_dict['class']['student']['marks']['history'])