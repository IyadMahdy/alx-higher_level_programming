#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is palindrome
 * @head: Pointer to head of list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *begin, *end, *prev;

	if (!(*head) || !((*head)->next))
		return (1);

	begin = *head;
	end = *head;

	while (end->next)
		end = end->next;

	while (begin != end && begin->next != end)
	{
		if (begin->n != end->n)
			return (0);
		prev = begin;
		while (prev->next != end)
			prev = prev->next;
		begin = begin->next;
		end = prev;

	}
	if (begin->n == end->n)
		return (1);
	return (0);
}
