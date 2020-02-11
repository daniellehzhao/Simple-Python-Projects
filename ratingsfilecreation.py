#Set of functions that record and average user responses to the Oscar Nominated movies from 2018. Assume that each record 
#includes 9 items. The first item should be the user number (starting with 1), and the remaining 8 should be a opinion from
#0 to 5 starts for each of 8 movies listed below. The fields should be as follows:
#user number starting with 1
#rating for Black Panther
#rating for BlacKkKlansman
#rating for Bohemian Rhapsody
#rating for The Favourite
#rating for Green Book
#rating for Roma
#rating for A Star Is Born
#rating for Vice
#Opinions numbers have the following interpretation:

#0: I did not see the movie
#1: Terrible
#2: Bad
#3: Average
#4: Good
#5: Fantastic

userinput=open('movie_ratings.tsv','w')

#function that will deal with adding more users

def get_more_ratings(inlist):
    usercomp=inlist
    user=0
    userratings=[]
    userresponse='y'
    while userresponse=='y':
        for num in usercomp: #ensures that the user number either starts from 1 if there is no previous user data, or starts from the number where left off
            if int(num[0])==1:
                user=int(num[0])+1
            elif int(num[0])>1:
                user=int(num[0])+1
            else:
                user+=1
        rating1= input('Did you see the movie Black Panther?' + '\n Enter a number from 0 to 5.\n' +'O means you did not see the movie'+ '\n Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic \n'+ 'What is your rating?')
                     
        rating2=input('Did you see the movie BlacKkKLansman?' + '\n Enter a number from 0 to 5.\n' +'O means you did not see the movie'+ '\n Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic \n'+ 'What is your rating?')
       
        rating3=input('Did you see the movie Bohemian Rhapsody?' + '\n Enter a number from 0 to 5.\n' +'O means you did not see the movie'+ '\n Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic \n'+ 'What is your rating?')
                      
        rating4=input('Did you see the movie The Favourite?' + '\n Enter a number from 0 to 5.\n' +'O means you did not see the movie'+ '\n Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic \n'+ 'What is your rating?')
                       
        rating5=input('Did you see the movie The Green Book?' + '\n Enter a number from 0 to 5.\n' +'O means you did not see the movie'+ '\n Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic \n'+ 'What is your rating?')
                      
        rating6=input('Did you see the movie Roma?' + '\n Enter a number from 0 to 5.\n' +'O means you did not see the movie'+ '\n Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic \n'+ 'What is your rating?')
                   
        rating7=input('Did you see the movie A Star is Born?' + '\n Enter a number from 0 to 5.\n' +'O means you did not see the movie'+ '\n Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic \n'+ 'What is your rating?')
                 
        rating8=input('Did you see the movie Vice?' + '\n Enter a number from 0 to 5.\n' +'O means you did not see the movie'+ '\n Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic \n'+ 'What is your rating?')             
        userratings.append([user,rating1,rating2,rating3,rating4,rating5,rating6,rating7,rating8])
        userresponse=input('Add one more user?')
        userresponse=userresponse[0].lower()
    return(userratings)

# function that gets and print the average of all the users' ratings
def get_average(listratings):
    blackpan=0
    klansman=0
    bohrap=0
    favourite=0
    greenbook=0
    roma=0
    starborn=0
    vice=0
    users=0
    seen1=0
    seen2=0
    seen3=0
    seen4=0
    seen5=0
    seen6=0
    seen7=0
    seen8=0
    for user in listratings:    
        if int(user[1])!=0:
            blackpan+=int(user[1])
            seen1+=1
        if int(user[2])!=0:
            klansman+=int(user[2])
            seen2+=1
        if int(user[3])!=0:
            bohrap+=int(user[3])
            seen3+=1
        if int(user[4])!=0:
            favourite+=int(user[4])
            seen4+=1
        if int(user[5])!=0:
            greenbook+=int(user[5])
            seen5+=1
        if int(user[6])!=0:
            roma+=int(user[6])
            seen6+=1
        if int(user[7])!=0:
            starborn+=int(user[7])
            seen7+=1
        if int(user[8])!=0:
            vice+=int(user[8])
            seen8+=1
    blackpan=blackpan/seen1
    klansman=klansman/seen2
    bohrap=bohrap/seen3
    favourite=favourite/seen4
    greenbook=greenbook/seen5
    roma=roma/seen6
    starborn=starborn/seen7
    vice=vice/seen8
    print('The movie Black Panther had an average score of '+ str(blackpan) +'. '+ str(seen1)+ ' people saw it in our sample.')
    print('The movie BlacKkKlansman had an average score of '+ str(klansman) +'. '+ str(seen2)+ ' people saw it in our sample.')
    print('The movie Bohemian Rhapsody had an average score of '+ str(bohrap) +'. '+ str(seen3)+ ' people saw it in our sample.')
    print('The movie The Favourite had an average score of '+ str(favourite) +'. '+ str(seen4)+ ' people saw it in our sample.')
    print('The movie Green Book had an average score of '+ str(greenbook) +'. '+ str(seen5)+ ' people saw it in our sample.')
    print('The movie Roma had an average score of '+ str(roma) +'. '+ str(seen6)+ ' people saw it in our sample.')
    print('The movie A Star Is Bor had an average score of '+ str(starborn) +'. '+ str(seen7)+ ' people saw it in our sample.')
    print('The movie Vice had an average score of '+ str(vice) +'. '+ str(seen8)+ ' people saw it in our sample.')
    
def average_movie_ratings(infile):
    user_ratings=[]
    i=0
    if infile.endswith('.tsv'):
        if os.path.isfile:
            ratingfile=open(infile,'r')
            for line in ratingfile:
                if i!=0:
                    rating=line.strip('\n').split('\t')
                    user_ratings.append(rating)
                    i+=1
                else:
                    i+=1
                    pass
    response=input("Add one more user? y/n")
    response=response[0].lower()
    if response=='y':
        more_data=get_more_ratings(user_ratings)
    for profile in more_data:
        user_ratings.append(profile)
    averages=get_average(user_ratings)
    ratefile=open(infile,'w')
    ratefile.write('User'+'\t'+'Black Panther'+'\t'+'BlacKkKlansman'+'\t'+'Bohemian Rhapsody'+'\t'+'The Favourite'+'\t'+'Green Book'+'\t'+'Roma'+'\t'+'A Star Is Born'+'\t'+'Vice'+'\n')
    for userprof in user_ratings:
        for rate in userprof:
            ratefile.write(str(rate) + '\t')
        ratefile.write('\n')
    ratefile.close()
    
        
    
    
    







        

       
        


