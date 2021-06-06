# Dictionary Attack on biis.buet.ac.bd

**<http://biis.buet.ac.bd/>** is used for academic purpose for the student from **Bangladesh University of Engineering and Technology.**

A user can try to login here multiple time without being locked or solving captcha. So, dictionary attack can be performned in this site.

## Preparation

At first, we have find the form elements which keep the userid and password. After reading the source code, I found that, there is two form elements, one is 'userName' and other is 'passWord'. But only userName element is used for keeping the userId. There is other element outside of the form named 'passwords' which is actually keeping the password. Then a javascript function performs RSA hash with the timestamp and save the value in 'passWord'. After this process, loginAction is called.

## Attack Plan

My plan is somehow set the value of 'userName' and 'passwords' element and click the login action fuction.
I write a python script which is using firefox web drive and selenium library. At first, I manually try to setup the value of these two elements and click the login button. Then I try to analysis the response. If it contains any message which can be found in a positive reply, our attack is successful.

## Attack

For this moment, I am trying to take input from the user. You have to run **Attack.py**.

## Future Plan

In real dictionary attack, there will be a dictionry which will try the possible passwords from the dictionry. It will be added in next step.

## Remarks

I just do this for fun. I think as one of the leading technical university, they should be aware of this type of security attack on their website.
