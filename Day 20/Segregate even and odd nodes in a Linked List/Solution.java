class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}

public class GfG {

    public static Node segregateEvenOdd(Node head) {
        Node resStart = null;
        Node resEnd = null;
        Node curr = head;
        Node prev = null;

        while (curr != null) {
            if (curr.data % 2 == 0) {
                if (prev != null) {
                    prev.next = curr.next;
                } else {
                    head = curr.next;
                }

                if (resStart == null) {
                    resStart = curr;
                    resEnd = resStart;
                } else {
                    resEnd.next = curr;
                    resEnd = resEnd.next;
                }

                curr = curr.next;
            } else {
                prev = curr;
                curr = curr.next;
            }
        }

        if (resStart == null) {
            return head;
        }

        resEnd.next = head;
        return resStart;
    }

    public static void printList(Node node) {
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
    }

    public static void main(String[] args) {
        Node head = new Node(0);
        head.next = new Node(1);
        head.next.next = new Node(4);
        head.next.next.next = new Node(6);
        head.next.next.next.next = new Node(9);
        head.next.next.next.next.next = new Node(10);
        head.next.next.next.next.next.next = new Node(11);

        System.out.print("Original Linked list: ");
        printList(head);

        head = segregateEvenOdd(head);

        System.out.print("\nModified Linked list: ");
        printList(head);
    }
}
