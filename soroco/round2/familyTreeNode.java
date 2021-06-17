import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.Map;
import java.util.Queue;
import java.util.HashMap;

class Node {
    String name;
    List<Node> children;
    List<Node> parents;

    public Node(String name){
        this.name = name;
        children = new ArrayList<>();
        parents = new ArrayList<>();
    }

    public void addChildren(Node child) {
        children.add(child);
    }

    public void addParent(Node parent) {
        parents.add(parent);
    }

}

class FamilyTree {
    private Map<String, Node> family;

    public FamilyTree() {
        family = new HashMap<>();
    }
    
    public void addRelation(String parent, String child) {
        if(!family.containsKey(parent)) {
            family.put(parent, new Node(parent));
        }

        if(!family.containsKey(child)) {
            family.put(child, new Node(child));
        }

        Node parentNode = family.get(parent);
        Node childNode = family.get(child);

        parentNode.addChildren(childNode);
        childNode.addParent(parentNode);
    }

    // Print child nodes in breadth first order
    public void fromNode(String name) {
        Node node = family.get(name);
        Queue<Node> queue = new LinkedList<>();
        queue.add(node);
        while(!queue.isEmpty()) {
            Node currentNode = queue.poll();
            System.out.println(currentNode.name + " ");

            for(Node child: currentNode.children) {
                queue.add(child);
            }            
        }
        System.out.println();
    }

    // Print parent nodes in breadth first order
    public void tillNode(String name) {
        Node node = family.get(name);
        Queue<Node> queue = new LinkedList<>();
        queue.add(node);
        while(!queue.isEmpty()) {
            Node currentNode = queue.poll();
            System.out.println(currentNode.name + " ");

            for(Node parent: currentNode.parents) {
                queue.add(parent);
            }            
        }
        System.out.println();
    }
}

public class FamilyTreeRunner {
    public static void main(String[] args) {
        FamilyTree familyTree = new FamilyTree();

        familyTree.addRelation("Bipin Singh", "Rajeev");
        familyTree.addRelation("Janki Devi", "Rajeev");

        familyTree.addRelation("Anil Rathore", "Risha");
        familyTree.addRelation("Pushpa Rathore", "Risha");

        familyTree.addRelation("Rajeev", "Ananya");
        familyTree.addRelation("Risha", "Ananya");

        familyTree.addRelation("Rajeev", "Radhi");
        familyTree.addRelation("Risha", "Radhi");

        // Example output
        familyTree.fromNode("Bipin Singh");
        familyTree.tillNode("Radhi");
    }
}