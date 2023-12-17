import java.util.*;


// Failed: Time Limit Exceeded
class FoodRatings_1 {
    private int length;
    private String[] foods;
    private String[] cuisines;
    private int[] ratings;
    

    public FoodRatings_1(String[] foods, String[] cuisines, int[] ratings) {
        this.foods = foods;
        this.cuisines = cuisines;
        this.ratings = ratings;
        this.length = foods.length;
    }

    public void changeRating(String food, int newRating) {
        for (int i=0; i<length; i++) {
            if (food.equals(foods[i])) {    // use equals() or compareTo() when comparing String type
                ratings[i] = newRating;
            }
        }
    }

    public String highestRated(String cuisine) {
        String food = foods[0];
        int rate = 0;
        for (int i=0; i<length; i++) {
            if (cuisine.equals(cuisines[i])) {  // use equals() or compareTo() when comparing String type
                if (ratings[i] > rate) {
                    food = foods[i];
                    rate = ratings[i];
                }
                else if (ratings[i] == rate) {
                    food = (food.compareTo(foods[i]) > 0) ? food = foods[i] : food;
                }
            }
        }
        return food;
    }
}


// use hashmap
// Failed: TLE
class FoodRatings_2 {
    private class Food {    // wrap properties
        String cuisine;
        int rating;

        Food(String cuisine, int rating) {
            this.cuisine = cuisine;
            this.rating = rating;
        }
    }

    private Map<String, Food> foodMap;

    public FoodRatings_2 (String[] foods, String[] cuisines, int[] ratings) {
        this.foodMap = new HashMap<>();
        for (int i=0; i<foods.length; i++) {
            foodMap.put(foods[i], new Food(cuisines[i], ratings[i]));
        }
    }

    public void changeRating(String food, int newRating) {
        if (foodMap.containsKey(food)) {
            Food f = foodMap.get(food);
            f.rating = newRating;
        }
    }

    public String highestRated(String cuisine) {
        String biggestFood = "A-SOUL";
        int biggestRate = 0;

        for (Map.Entry<String, Food> entry : foodMap.entrySet()) {
            Food f = entry.getValue();
            if (f.cuisine.equals(cuisine) && (f.rating > biggestRate || (f.rating == biggestRate && entry.getKey().compareTo(biggestFood)<0))) {
                biggestFood = entry.getKey();
                biggestRate = f.rating;
            }
        }
        return biggestFood;
    }
}


// Failed: Time Limit Exceeded
class FoodRatings {
    private int length;
    private String[] foods;
    private String[] cuisines;
    private int[] ratings;
    private ArrayList<String> cuisineTypes;
    private ArrayList<Integer> highestRatedFoodIndex;
    

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        this.foods = foods;
        this.cuisines = cuisines;
        this.ratings = ratings;
        this.cuisineTypes = new ArrayList<>();
        this.highestRatedFoodIndex = new ArrayList<>();
        for (String c : cuisines) {
            boolean contains = false;
            for (String type : cuisineTypes) {
                if (c.equals(type)) {
                    contains = true;
                    break;
                }
            }
            if (!contains) {
                this.cuisineTypes.add(c);
                String food = foods[0];
                int rate = 0;
                int index = 0;
                for (int i=0; i<length; i++) {
                    if (c.equals(cuisines[i])) {
                        if (ratings[i] > rate) {
                            food = foods[i];
                            rate = ratings[i];
                            index = i;
                        }
                        else if (ratings[i] == rate) {
                            index = (food.compareTo(foods[i]) > 0) ? i : index;
                        }
                    }
                }
                this.highestRatedFoodIndex.add(index);
            }
        }
    }

    public void changeRating(String food, int newRating) {
        for (int i=0; i<length; i++) {
            if (food.equals(foods[i])) {
                ratings[i] = newRating;

                String cuisine = cuisines[i];
                
                for (int j=0; j<cuisineTypes.size(); j++) {
                    if (cuisineTypes.get(j).equals(cuisine)) {
                        if (ratings[highestRatedFoodIndex.get(j)] < newRating) {
                            highestRatedFoodIndex.set(j, i);
                            break;
                        }
                        else if (ratings[highestRatedFoodIndex.get(j)] == newRating && foods[highestRatedFoodIndex.get(j)].compareTo(food) > 0) {
                            highestRatedFoodIndex.set(j, i);
                            break;
                        }
                    }
                }
            }
        }
    }

    public String highestRated(String cuisine) {
        String food = "A-SOUL";
        for (int i=0; i<cuisineTypes.size(); i++) {
            if (cuisineTypes.get(i).equals(cuisine)) {
                food = foods[highestRatedFoodIndex.get(i)];
                break;
            }
        }
        return food;
    }
}