package com.echonest.knowledge.hashr;

import java.util.Arrays;

/**
 * Created by devstation2 on 8/19/15.
 */
public class Test {

    public static void main(String[] args) throws Exception{
        int size = 5000000;
        int[] arr = new int[size];

        while (true) {
            long before = System.currentTimeMillis();
            for (int i = 0; i < 2000000000; i++) {
                arr[2]++;
            }
            long after = System.currentTimeMillis();
            System.out.println("Elapsed 2: " + (after - before));
            Thread.sleep(1000);


            before = System.currentTimeMillis();
            for (int i = 0; i < 2000000000; i++) {
                arr[1] = arr[1] + 1;
            }
            after = System.currentTimeMillis();
            System.out.println("Elapsed 1: " + (after - before));
            Thread.sleep(1000);


        }

    }
}
