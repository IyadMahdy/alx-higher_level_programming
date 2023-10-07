#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: Pointer to head of list
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;

	fast = list;
	while (fast->next != NULL && fast != NULL)
	{
		fast = fast->next->next;
		list = list->next;

		if (fast == list)
			return (1);
	}
	return (0);
}
