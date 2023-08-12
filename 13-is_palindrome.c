#include "lists.h"

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * copy_in_reverse - copies list but with reversed values
 * @h: list destination
 * Return: begining of new list
 */
listint_t *copy_in_reverse(listint_t *h)
{
	listint_t *new = NULL, *top = NULL;

	while (h)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
		{
			if (top)
				free_listint(top);
			return (NULL);
		}
		new->n = h->n;
		new->next = top;
		top = new;
		h = h->next;
	}
	return (top);
}

/**
 * is_palindrome - tests whether linked list is a palindrome
 * @head: beginning of list
 * Return: 0 if not palindrome, 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *tmp2, *hold = NULL;

	if (!(*head))
		return (1);

	hold = copy_in_reverse(*head);
	if (!hold)
		return (0);

	tmp2 = hold;
	while (tmp && tmp2)
	{
		if (tmp->n != tmp2->n)
		{
			free_listint(hold);
			return 0;
		}
		tmp = tmp->next;
		tmp2 = tmp2->next;
	}
	free_listint(hold);
	return (1);
}

