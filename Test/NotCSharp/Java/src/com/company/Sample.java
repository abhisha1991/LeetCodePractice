package com.company;

import java.util.Scanner;

/**
 * Created by abhisha on 7/9/2017.
 */
public class Sample {

    public void sampleFunc()
    {
        System.out.println("Enter your name: ");
        Scanner scan = new Scanner(System.in);
        String name = scan.next();
        System.out.println("Your name is: " + name);
        System.out.println("Enter your age: ");
        scan = new Scanner(System.in);
        int age = scan.nextInt();
        System.out.println("Your age is: " + age);
        System.out.print(0);
    }
}
