#include "lists.h"
#include <stdlio.h>

/**
 * check_cycle - Function checks if the list has a cycle.
 * @list: Pointer to the list.
 *
 * Return: 1 if there is a cycle or 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	while (current && check->next)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
