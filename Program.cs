using System;

namespace UserPassBlackjack
{
    class Program
    {
        static void HigherLower(string userName, string userPass, int userHigh) {
            Console.Write("Would you like to play a round of Higher/Lower? (Y/N) ");
            string play = Console.ReadLine();
            if (play.ToLower() == "y") {
                Random rnd = new Random();
                int randomNumber = rnd.Next(1, 101);
                Console.WriteLine("I have chosen a random number between 1 and 100, guess what it is.");
                int guess = 101;
                int guesses = 1;
                do {
                    try {
                        guess = Convert.ToInt32(Console.ReadLine());
                        if (1 > guess || guess > 100)
                            Console.WriteLine("Please enter a number in the range.");
                        else {
                            if (guess == randomNumber) {
                                Console.Write($"Good job, you guessed that in {guesses} guesses! ");
                                if (guesses < userHigh) {
                                    userHigh = guesses;
                                    Console.WriteLine("That's a new highscore!");
                                }
                                else
                                    Console.WriteLine();
                            }
                            else {
                                string HL = (randomNumber > guess) ? "Your guess is too low." : "Your guess is too high.";
                                Console.WriteLine(HL);
                                guesses++;
                            }
                        }
                    }
                    catch {
                        Console.WriteLine("Please enter a number.");
                    }
                } while (guess != randomNumber);
            }
            //else if (play.ToLower() == "n")
                //Main(userSave);
            else
                Console.WriteLine("Please enter a Y or an N");
        }
        static void Main(string[] args) {
            string[,] userPass = new string[100, 3];
            userPass[0, 0] = "Joel";
            userPass[0, 1] = "12345";
            userPass[0, 2] = "1";
            int l = 0;
            while (1 == 1) {
                Console.WriteLine("Would you like to create an account (1), login (2), or exit (3)");
                string option = Console.ReadLine();
                if (option == "1") {
                    string username, password = " ";
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
                    Console.WriteLine("The password is accepted.");
                    userPass[l, 0] = username;
                    userPass[l, 1] = password;
                    userPass[l, 2] = "100";
                }
                else if (option == "2") {
                    Console.Write("Enter your username: ");
                    string userattempt = Console.ReadLine();
                    int user = 0;
                    for (user = 0; user < 100; user++) {
                        if (userPass[user, 0] == userattempt) {
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
                                HigherLower(userPass[user, 0], userPass[user, 1], Convert.ToInt32(userPass[user, 2]));
                                Console.WriteLine("Thank you for playing!");
                                break;
                            }
                            Console.Write("The password is incorrect. Please try again. ");
                        }
                        Console.Clear();
                        Console.WriteLine("You took too many guesses.");
                    }
                    else
                        Console.WriteLine("That username does not exist.");
                }
                else if (option == "3")
                    break;
                else {
                    Console.Clear();
                    Console.WriteLine("Please enter something that is in the program; 1, 2, or 3.");
                }
            }
            Console.WriteLine("Thank you for using this program.");
        }
    }
}