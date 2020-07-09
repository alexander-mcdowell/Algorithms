import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

/*
Banzhaf algorithm: computes the Banzhaf Power Index of a selection of voters; shows who has the most power in an election.
Requirements: There must be a certain threshold (quota) of votes for a particular vote to pass.
Method:
    1. Using a Monte-Carlo method, generate a random coalition (subset of voters who support a particular vote) of voters excluding the voter whose index is being calculated.
    1 cont. For example, if the voters are [A, B, C, D] and you are testing A"s power, a random coalition would be (C, D).
    2. A winning coalition is a coalition whose total votes exceed the threshold for a vote to pass.
    2 cont. If A has 4 votes, B has 3 votes, C has 2 votes, and D has 1 vote and the threshold is 6, then (A, B), (A, C), (A, B, D) are winning coalitions
    3. If the random coalition does not pass the threshold, but passes if the voter being tested joins the coalition, increment a "winning counter".
    3 cont. For example, coalition (B, C) does not pass the threshold, but (A, B, C) does. Thus, increment A"s winning counter.
    4. The Banzhaf index of the winner is thus the winning counter divided by the coalitions tested.
*/

class Banzahf {
    private static String[] randomSubset(String set[]) {
        ArrayList<String> subsets = new ArrayList<String>();
        int randomValue;
        for (String s : set) {
            randomValue = ThreadLocalRandom.current().nextInt(0, 2);
            if (randomValue == 0) subsets.add(s);
        }
        String[] subsetsArray = new String[subsets.size()];
        for (int i = 0; i < subsets.size(); i++) subsetsArray[i] = subsets.get(i);
        return subsetsArray;
    }
    
    private static int getIndex(String[] strArray, String x) {
        for (int index = 0; index < strArray.length; index++) {
            if (strArray[index] == x) return index;
        }
        // Return -1 if x is not in strArray
        return -1;
    }

    public static double BanzhafMeasure(String voter, String[] voters, int[] weights, int quota, int tries) {
        
        int n = 0;
        int votes;
        String[] coalition;

        for (int k = 0; k < tries; k++) {
            if (k > tries) break;
            coalition = randomSubset(voters);
            votes = 0;
            for (String x : coalition) votes += weights[getIndex(voters, x)];
            if ((votes < quota) && (votes + weights[getIndex(voters, voter)] >= quota)) {
                n += 1;
            }
        }
        return ((double) n / tries);
    }
    public static void main(String[] args) {
        // keys and values form a dictionary where the keys are states of the U.S. and the values are delegates in the electoral college.
        String[] keys = {"Alabama", "Alaska", "Arizona", "Arkansas", "California",
                        "Colorado", "Connecticut", "D.C", "Delaware", "Florida",
                        "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
                        "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
                        "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
                        "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
                        "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
                        "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
                        "Washington", "West Virginia", "Wisconsin", "Wyoming"};
        int[] values = {9, 3, 10, 6, 55, 9, 7, 3, 3, 27, 15, 4, 4, 21, 11, 7, 6, 8, 9, 4, 10, 12, 17, 10, 6, 11, 3, 5, 5, 4, 15, 5, 31, 15, 3, 20, 7, 7, 21, 4, 8, 3, 11, 34, 5, 3, 13, 11, 5, 10, 3};

        int quota = 270;
        double accuracy = 0.95;
        double eta = 0.01;
        int iterations = (int) Math.ceil(Math.log(2 / (1 - accuracy)) / (2 * eta * eta));

        double banzahfPower;

        Object[][] displayTable = new Object[keys.length + 1][3];
        displayTable[0] = new String[] {"State Name", "Electoral Votes", "Banzhaf Measure (Voting Power)"};
        for (int i = 0; i < keys.length; i++) {
            banzahfPower = BanzhafMeasure(keys[i], keys, values, quota, iterations);
            displayTable[i + 1] = new Object[] {keys[i], 
                                                values[i], 
                                                banzahfPower};
        }
        for (Object[] row : displayTable) {
            System.out.format("%15s     %15s     %15s\n", row);
        }
    }
}