class Multifunction():

    def Subfields1():
        A = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        x=input('')

        for i in ((A)):
            print(i)
            
    def OddEven():
        num = (int(input('enter the num')))

        if (num%2==0):
            print(num,'is even num')
        else:
            print(num,'is odd num')
        
        
    def eligible():

        Gender = input('Enter your Gender: ')
        Age = int(input('Enter the age: '))

        if (Gender=='male'):
            if(Age>=21):
                print('Eligible for Marraige')
            else:
                print('Not eligible')
        elif (Gender=='female'):
            if(Age>=18):
                print('Eligible for Marraige')
            else:
                print('Not eligible')
    
    
    
    def score():
        sub1=int(input('Enter your mark:'))
        sub2=int(input('Enter your mark:'))
        sub3=int(input('Enter your mark:'))

        subjects =[sub1,sub2,sub3]
        subjects
        total=0

        for i in subjects:
            total+=i
        print('total:',total)
        print('percentage:',total/3)
    

    
    
    def triangle():
        height = int(input('Enter the height: '))
        breath = int(input('Enter the breath: '))

        area = (height * breath) / 2
        print('Triangle area: (height * breath)/2')
        print('Area of triangle:', area)

        height1 = int(input('Enter the height1: '))
        height2 = int(input('Enter the height2: '))
        breath = int(input('Enter the breath: '))

        perimeter = height1 + height2 + breath
        print('Triangle perimeter: (height1 + height2 + breath)')
        print('Perimeter of triangle:', perimeter)
    