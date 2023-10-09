#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: Pointer to head of list
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list)
		return (0);

	fast = list;
	slow = list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
