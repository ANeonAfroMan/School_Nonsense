using System;

namespace UserPassBlackjack
{
    class Program
    {
        static void Main(string[] args) {
            string[,] userPass = new string[100,3];
            userPass[0, 0] = "Joel";
            userPass[0, 1] = "12345";
            userPass[0, 2] = "1";
            int l = 0;
            while (1 == 1) {
                Console.WriteLine("Would you like to create an account (1), login (2), or exit (3)");
                string option = Console.ReadLine();
                if (option == "1") {
                    string username , password = " ";
                    bool hasCapital, hasLower, hasNumber, hasSpecial;
                    do {
                        Console.Write("Enter your username: ");
                        username = Console.ReadLine();
                        if (username.Length < 6)
                            Console.WriteLine("Please enter a username that is at least 6 characters long.");
                        else {
                            do {
                                Console.Write("Enter your password: ");
                                password = Console.ReadLine();
                                hasCapital = false;
                                hasLower = false;
                                hasNumber = false;
                                hasSpecial = false;
                                foreach (char x in password) {
                                    try {
                                        Convert.ToInt32(x.ToString());
                                        hasNumber = true;
                                    }
                                    catch {
                                        if (Convert.ToString(x) == x.ToString().ToUpper() && !(Convert.ToString(x) == x.ToString().ToLower()))
                                            hasCapital = true;
                                        else if (Convert.ToString(x) == x.ToString().ToLower() && !(Convert.ToString(x) == x.ToString().ToUpper()))
                                            hasLower = true;
                                        else
                                            hasSpecial = true;
                                    }
                                }
                                if (!(hasCapital && hasLower && hasNumber && hasSpecial))
                                    Console.WriteLine("Your password needs: ");
                                if (password.Length < 8)
                                    Console.WriteLine("- To be at least 8 characters long.");
                                if (!(hasCapital && hasLower))
                                    Console.WriteLine("- At least one capital and lowercase letter.");
                                if (!(hasNumber))
                                    Console.WriteLine("- At least one number.");
                                if (!(hasSpecial))
                                    Console.WriteLine("- At least one special character.");
                            }
                            while (password.Length < 8 && !(hasCapital && hasLower && hasNumber && hasSpecial));
                        }
                    } 
                    while (username.Length < 6);
                    l++;
                    userPass[l, 0] = username;
                    userPass[l, 1] = password;
                    userPass[l, 2] = "0";
                }
                else if (option == "2") {
                    Console.Write("Enter your username: ");
                    string userattempt = Console.ReadLine();
                    int user = 0;
                    for (user = 0; user < 100; user++) {
                        if (userPass[user,0] == userattempt) {
                            break;
                        }
                    }
                    if (user != 100) {
                        Console.Write("Enter your password: ");
                        for (int loop = 0; loop < 5; loop++) {
                            string passattempt = Console.ReadLine();
                            if (userPass[user, 1] == passattempt) {
                                Console.Clear();
                                Console.WriteLine($"Welcome to your account! Your highscore is {userPass[user, 2]}");
                                while (true) {
                                    Console.Write("Would you like to play a game? (Y/N) ");
                                    string play = Console.ReadLine();
                                    if (play.ToLower() == "y") {
                                        //make my own at some point
                                        string playAgain = "yes";
                                        Console.WriteLine("Welcome to Ethan's game of higher/lower!");
                                        int wager;
                                        while (playAgain == "yes") {
                                            Random rnd = new Random();
                                            int randomNumber = rnd.Next(1, 101);
                                            Console.Write("Would you like to wager in a game of higher lower (yes/no): ");
                                            string yesNo = Console.ReadLine();
                                            yesNo = yesNo.ToLower();
                                            Console.Clear();

                                            if (yesNo == "yes") {

                                                Console.Write("How much would you like to wager($1-$100): ");
                                                wager = Convert.ToInt32(Console.ReadLine());
                                                Console.WriteLine($"If you win, you could earn ${wager * 5}");
                                            }
                                            Console.WriteLine("Let's move onto the rules ");
                                            Console.WriteLine("You will have 5 guesses to get the number that is ranged from 1-100");
                                            Console.WriteLine("After you guess, I will output higher or lower to indicate if you need to increase or decrease your guess");
                                            Console.WriteLine("Click enter to continue: ");
                                            string enter = Console.ReadLine();
                                            Console.Clear();

                                            Console.WriteLine("Lets get started!");

                                            Console.Write("Pick a number 1-100: ");
                                            int num = Convert.ToInt32(Console.ReadLine());


                                            for (int x = 1; x < 5; x++) {
                                                if (num > randomNumber) {
                                                    Console.WriteLine("Lower");
                                                }
                                                else if (num < randomNumber) {
                                                    Console.WriteLine("Higher");
                                                }
                                                else if (num == randomNumber) {
                                                    Console.WriteLine("You win!!!!");
                                                    Console.WriteLine($"My number was {num}");
                                                    break;
                                                }
                                                else if (num >= 100) {
                                                    Console.WriteLine("You cannot pick a number higher than 100, now you lose a turn.");
                                                }
                                                else if (num < 0) {
                                                    Console.WriteLine("You cannot pick a number lower than 1, now you lose a turn.");
                                                }
                                                else if (x == 5 && num == randomNumber) {
                                                    Console.WriteLine("You win!!!!");
                                                    Console.WriteLine($"My number was {num}");
                                                    break;
                                                }

                                                Console.Write("Pick another number 1-100: ");
                                                num = Convert.ToInt32(Console.ReadLine());

                                            }

                                            if (num != randomNumber) {
                                                Console.WriteLine($"My number was {randomNumber}, so you lose.");

                                            }
                                            Console.WriteLine("Would you like play again.");
                                            Console.Write("Enter yes to play again and no to quit: ");
                                            playAgain = Console.ReadLine();
                                            if (playAgain == "yes" && playAgain == "no") {
                                                break;
                                            }
                                            Console.Clear();
                                        }
                                        //ends here
                                    }
                                    else if (play.ToLower() == "n")
                                        break;
                                    else
                                        Console.WriteLine("Please enter a y or an n");
                                }
                                break;
                            }
                            Console.Write("The password is incorrect. Please try again. ");
                        }
                    }
                    else
                        Console.WriteLine("That username does not exist.");
                }
                else if (option == "3")
                    break;
                else {
                    Console.Clear();
                    Console.WriteLine("Please enter something that is in the program; 1 or 2.");
                }
            }
        }
    }
}