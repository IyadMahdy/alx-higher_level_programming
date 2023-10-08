#include "lists.h"

/**
 * insert_node - inserts node to a sorted linked list
 * @head: Pointer to the head pointer to list
 * @number: Number to insert into the list
 *
 * Return: Address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *fast, *slow, *new;

	if (!head || !number)
		return (NULL);

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	slow = *head;
	if (!slow)
	{
		*head = new;
		return (new);
	}
	if (slow->n >= number)
	{
		new->next = slow;
		*head = new;
		return (new);
	}
	fast = slow->next;
	while (fast)
	{
		if (number >= slow->n && number <= fast->n)
		{
			new->next = fast;
			slow->next = new;
			return (new);
		}
		slow = slow->next;
		fast = fast->next;
	}
	slow->next = new;
	return (new);
}
