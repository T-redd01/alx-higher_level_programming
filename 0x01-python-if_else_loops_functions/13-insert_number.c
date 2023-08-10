#include "lists.h"

/**
 * insert_node - insert a node in an oredered linked list
 * @head: list to insert node into
 * @number: content inside node
 * Return: new node on success, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *curr = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!(*head) || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (curr)
	{
		if (!(curr->next))
			break;
		if (curr->next->n > number)
		{
			new->next = curr->next;
			curr->next = new;
			return (new);
		}
		curr = curr->next;
	}
	curr->next = new;
	return (new);
}

