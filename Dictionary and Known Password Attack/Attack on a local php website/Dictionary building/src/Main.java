// Java program to calculate SHA-1 hash value 

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class  Main{
    public static String encryptThisString(String input)
    {
        try {
            // getInstance() method is called with algorithm SHA-1 
            MessageDigest md = MessageDigest.getInstance("SHA-1");

            // digest() method is called 
            // to calculate message digest of the input string 
            // returned as array of byte 
            byte[] messageDigest = md.digest(input.getBytes());

            // Convert byte array into signum representation 
            BigInteger no = new BigInteger(1, messageDigest);

            // Convert message digest into hex value 
            String hashtext = no.toString(16);

            // Add preceding 0s to make it 32 bit 
            while (hashtext.length() < 32) {
                hashtext = "0" + hashtext;
            }

            // return the HashText 
            return hashtext;
        }

        // For specifying wrong message digest algorithms 
        catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    // Driver code 
    public static void main(String args[]) throws
             IOException {
        String row;
        FileWriter csvWriter = new FileWriter("D:\\LEVEL 4 TERM 1\\Dictionary-attack\\hashed_dictionary.csv");
        BufferedReader csvReader = new BufferedReader(new FileReader("D:\\LEVEL 4 TERM 1\\Dictionary-attack\\dictionary.csv"));
        while ((row = csvReader.readLine()) != null) {
            String[] data = row.split(",");

            csvWriter.append(data[0]+","+encryptThisString(data[0])+"\n");
        }
        csvReader.close();
        csvWriter.flush();
        csvWriter.close();




    }
} 