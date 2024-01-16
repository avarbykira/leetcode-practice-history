// Link: https://leetcode.com/problems/insert-delete-getrandom-o1

import java.util.*;

class RandomizedSet {

    private Map<Integer, Integer> memory;
    private ArrayList<Integer> list;

    public RandomizedSet() {
        this.memory = new HashMap<Integer, Integer>();
        this.list = new ArrayList<Integer>();
    }
    
    public boolean insert(int val) {
        if (memory.containsKey(val)) {
            return false;
        }
        else {
            this.list.add(val);
            this.memory.put(val, list.size()-1);
            return true;
        }
        
    }
    
    public boolean remove(int val) {
        if (!memory.containsKey(val)) {
            return false;
        }
        else {
            int index = memory.get(val);
            list.set(index, list.get(list.size()-1));
            // wrong position
            memory.put(list.get(index), index);
            list.remove(list.size()-1);
            memory.remove(val); // change it to here passed. but why? because val and list.size()-1 may be the same!
            return true;
        }
    }
    
    public int getRandom() {
        Random rand = new Random();
        return list.get(rand.nextInt(list.size()));
    }
}