import java.util.ArrayList;

// Dictionary objects act like dicts in python
class Dictionary {
    public ArrayList<Object> keys;
    public ArrayList<Object> values;

    public Dictionary() {
        keys = new ArrayList<Object>();
        values = new ArrayList<Object>();
    }

    public void add(Object key, Object value) {
        keys.add(key);
        value.add(value);
    }

    public Object get(Object key) {
        for (int i = 0; i < keys.length; i++) {
            if (keys.get(i).equals(key)) return value.get(i);
        }
    }

    public void remove(Object key) {
        for (int i = 0; i < keys.length; i++) {
            if (keys.get(i).equals(key)) {
                keys.remove(key);
                values.remove(i);
            }
        }
    }

    // Checks if a particular key is in the dict
    public boolean in(Object key) { return keys.contains(key); }
}