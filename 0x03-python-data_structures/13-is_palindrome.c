#include "lists.h"
/**
 * free_listint - Reverses a linked list.
 * @head: The pointer to a node in the list.
 *
 * Return: Pointer the new list.
 */
void free_listint(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return;

    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer of  the linked list.
 *
 * Return: 1 if it is a palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *temp = *head, *reversed_second_half = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    while (fast && fast->next)
    {
        fast = fast->next->next;

        if (!fast)
            reversed_second_half = slow->next;
        else if (!fast->next)
            reversed_second_half = slow->next->next;

        slow = slow->next;
    }

    reverse_listint(&reversed_second_half);

    while (reversed_second_half && temp)
    {
        if (temp->n != reversed_second_half->n)
            return 0;

        reversed_second_half = reversed_second_half->next;
        temp = temp->next;
    }

    return 1;
}
