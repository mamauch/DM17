import weka.associations.FPGrowth;
import weka.core.Instances;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import weka.core.converters.ConverterUtils.DataSource;
import weka.associations.FPGrowth;
import weka.core.Instances;



public class FPGrowthDataSets {
    public static void main(String[] args) throws Exception {
        File dm1 = new File("/Users/Marius/Documents/Studium/Mainz/DM17/Uebung3/Nr2Weka/FPGrowth/data/dm1.arff");
        File dm2 = new File("/Users/Marius/Documents/Studium/Mainz/DM17/Uebung3/Nr2Weka/FPGrowth/data/dm2.arff");
        File dm3 = new File("/Users/Marius/Documents/Studium/Mainz/DM17/Uebung3/Nr2Weka/FPGrowth/data/dm3.arff");
        File dm4 = new File("/Users/Marius/Documents/Studium/Mainz/DM17/Uebung3/Nr2Weka/FPGrowth/data/dm4.arff");
        File movie = new File("/Users/Marius/Documents/Studium/Mainz/DM17/Uebung3/Nr2Weka/FPGrowth/data/movielens-converted.arff");

        BufferedReader readerdm1 = new BufferedReader(new FileReader(dm1));
        BufferedReader readerdm2 = new BufferedReader(new FileReader(dm2));
        BufferedReader readerdm3 = new BufferedReader(new FileReader(dm3));
        BufferedReader readerdm4 = new BufferedReader(new FileReader(dm4));
        BufferedReader readermovie = new BufferedReader(new FileReader(movie));

        Instances datadm1 = new Instances(readerdm1);
        Instances datadm2 = new Instances(readerdm2);
        Instances datadm3 = new Instances(readerdm3);
        Instances datadm4 = new Instances(readerdm4);
        Instances datamovie = new Instances(readermovie);

        FPGrowth fpGrowthdm1 = new FPGrowth();
        FPGrowth fpGrowthdm2 = new FPGrowth();
        FPGrowth fpGrowthdm3 = new FPGrowth();
        FPGrowth fpGrowthdm4 = new FPGrowth();
        FPGrowth fpGrowthmovie = new FPGrowth();

        long startTime = System.currentTimeMillis();
        long stopTime = System.currentTimeMillis();
        long elapsedTime = stopTime - startTime;

        for (double i = 0.4; i<1; i=i+0.1) {

            fpGrowthdm1.setLowerBoundMinSupport(i);
            fpGrowthdm2.setLowerBoundMinSupport(i);
            fpGrowthdm3.setLowerBoundMinSupport(i);
            fpGrowthdm4.setLowerBoundMinSupport(i);
            fpGrowthmovie.setLowerBoundMinSupport(i);

            startTime = System.currentTimeMillis();
            fpGrowthdm1.buildAssociations(datadm1);
            stopTime = System.currentTimeMillis();
            elapsedTime = stopTime - startTime;
            System.out.println(i);
            System.out.println(elapsedTime);
            System.out.println("dm1");

            startTime = System.currentTimeMillis();
            fpGrowthdm2.buildAssociations(datadm2);
            stopTime = System.currentTimeMillis();
            elapsedTime = stopTime - startTime;
            System.out.println(i);
            System.out.println(elapsedTime);
            System.out.println("dm2");

            startTime = System.currentTimeMillis();
            fpGrowthdm3.buildAssociations(datadm3);
            stopTime = System.currentTimeMillis();
            elapsedTime = stopTime - startTime;
            System.out.println(i);
            System.out.println(elapsedTime);
            System.out.println("dm3");

            startTime = System.currentTimeMillis();
            fpGrowthdm4.buildAssociations(datadm4);
            stopTime = System.currentTimeMillis();
            elapsedTime = stopTime - startTime;
            System.out.println(i);
            System.out.println(elapsedTime);
            System.out.println("dm4");

            startTime = System.currentTimeMillis();
            fpGrowthmovie.buildAssociations(datamovie);
            stopTime = System.currentTimeMillis();
            elapsedTime = stopTime - startTime;
            System.out.println(i);
            System.out.println(elapsedTime);
            System.out.println("movie");
        }

    }
}
