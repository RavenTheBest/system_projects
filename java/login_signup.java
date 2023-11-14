import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class UserAuthentication {

    static Map<String, Map<String, String>> data = new HashMap<>();
    static boolean logged = false;
    static String username = "";

    public static boolean checkLogin(String user, String pwd) {
        return data.containsKey(user) && data.get(user).get("password").equals(pwd);
    }

    public static boolean checkValidation(String user, String pwd, String confirmPwd) {
        if (pwd.equals(confirmPwd) && !data.containsKey(user)) {
            data.put(user, new HashMap<>());
            data.get(user).put("password", pwd);
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String defaultText = "[1] Login\n[2] Signup\n";

        while (true) {
            while (!logged) {
                System.out.println(defaultText);
                System.out.print("Choose: ");
                String option = scanner.nextLine();

                if (option.equals("1")) {
                    System.out.print("Username: ");
                    String user = scanner.nextLine();
                    System.out.print("Password: ");
                    String pwd = scanner.nextLine();
                    boolean check = checkLogin(user, pwd);

                    if (check) {
                        username = user;
                        logged = true;
                    } else {
                        System.out.println("Invalid username or password");
                    }
                } else if (option.equals("2")) {
                    System.out.print("Username: ");
                    String user = scanner.nextLine();
                    System.out.print("Password: ");
                    String pwd = scanner.nextLine();
                    System.out.print("Confirm password: ");
                    String confirmPwd = scanner.nextLine();
                    boolean valid = checkValidation(user, pwd, confirmPwd);

                    if (valid) {
                        username = user;
                        logged = true;
                        System.out.println("Account created successfully");
                    } else if (data.containsKey(user)) {
                        System.out.println("Username already exists!");
                    } else {
                        System.out.println("Passwords don't match");
                    }
                } else {
                    System.out.println("Invalid option");
                }
            }

            while (logged) {
                System.out.println("Hello, " + username + "!");
                System.out.println("[1] Logout\n");
                System.out.print("Choose: ");
                String option = scanner.nextLine();

                if (option.equals("1")) {
                    username = "";
                    logged = false;
                } else {
                    System.out.println("Invalid input!");
                }
            }
        }
    }
                }
