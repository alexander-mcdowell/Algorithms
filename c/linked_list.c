#include <stdio.h>
#include <stdlib.h>

struct linked_list {
    int value;
    struct linked_list* next;
};

void pushVal(struct linked_list* list_address, int value) {
    struct linked_list* ptr = list_address;

    while (ptr->next != NULL) {
        ptr = ptr->next;
    }

    ptr->next = (struct linked_list*) malloc(sizeof(struct linked_list));
    ptr->next->value = value;
    ptr->next->next = NULL;
}

void pushValues(struct linked_list* list_address, int values[], int arrayLength) {
    struct linked_list* ptr = list_address;
    for (int i = 0; i < arrayLength; i++) {
        while (ptr->next != NULL) {
            ptr = ptr->next;
        }

        ptr->next = (struct linked_list*) malloc(sizeof(struct linked_list));
        ptr->next->value = values[i];
        ptr->next->next = NULL;
    }
}

void print(struct linked_list* list_address) {
    struct linked_list* ptr = list_address;

    while (ptr != NULL) {
        printf("%d -> ", ptr->value);
        ptr = ptr->next;
    }
    (void) printf("NULL\n");
}

struct linked_list find(struct linked_list* list_address, int value) {
    struct linked_list* ptr = list_address;

    while (ptr->next != NULL) {
        if (ptr->value == value) {
            return *ptr;
        }
        ptr = ptr->next;
    }
    (void) printf("Could not find the value %d in the linked list.", value);
    // Return the original list if the value could not be found
    return *(list_address);
}

// Cannot insert to front
void insert(struct linked_list* list_address, int value, int index) {
    struct linked_list* ptr = list_address;
    struct linked_list* old;
    int i = 0;

    while (ptr->next != NULL) {
        if (i == index - 1) break;
        ptr = ptr->next;
        i++;
    }
    if (ptr->next == NULL) {
        ptr->next = (struct linked_list*) malloc(sizeof(struct linked_list));
        ptr->next->value = value;
        ptr->next->next = NULL;
    }
    else {
        old = ptr->next;
        ptr->next = (struct linked_list*) malloc(sizeof(struct linked_list));
        ptr->next->value = value;
        ptr->next->next = old;
    }
}

// Returns the new front of the list
struct linked_list* addToFront(struct linked_list* list_address, int value) {
    struct linked_list* ptr = (struct linked_list*) malloc(sizeof(struct linked_list));
    ptr->next = list_address;
    ptr->value = value;
    return ptr;
}

struct linked_list pop(struct linked_list* list_address, int index) {
    struct linked_list* ptr = list_address;
    struct linked_list* prev = NULL;
    int i = 0;
    while (ptr->next != NULL) {
        if (i == index) break;
        prev = ptr;
        ptr = ptr->next;
        i++;
    }
    struct linked_list removed;
    if (ptr->next != NULL) {
        prev->next = ptr->next;
        removed = *ptr;
        free(ptr);
    }
    return removed;
}

int main(int argc, char *argv[]) {
    struct linked_list* root = (struct linked_list*) malloc(sizeof(struct linked_list));
    root->value = 0;
    int values[] = {1, 2, 3, 4};
    pushVal(root, 10);
    print(root);
    pushValues(root, values, sizeof(values) / sizeof(values[0]));
    insert(root, 7, 1);
    root = addToFront(root, -1);
    print(root);
    (void) printf("Popped value: %d\n", pop(root, 3).value);
    print(root);
    return 0;
}