#include "lists.h"

/**
 * reverse_from_middle - Reverses the second half of a list
 * @head: head of list
 *
 * Return: New head of list
 */
listint_t *reverse_from_middle(listint_t *head)
{
	listint_t *fast, *slow, *h, *tmp;

	fast = head;
	slow = head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	h = NULL;
	while (slow)
	{
		tmp = slow;
		slow = slow->next;
		tmp->next = h;
		h = tmp;
	}

	return (h);
}

/**
 * is_palindrome - Checks if a singly linked list is palindrome
 * @head: Pointer to head of list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *p1, *p2;

	if (!(*head) || !((*head)->next))
		return (1);

	p1 = *head;
	p2 = reverse_from_middle(p1);

	while (p2)
	{
		if (p1->n != p2->n)
			return (0);
		p1 = p1->next;
		p2 = p2->next;
	}

	return (1);
}
