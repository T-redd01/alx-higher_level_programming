#include "lists.h"

/**
 * is_palindrome - checks whether list is a palindrome
 * @head: beginning of list
 *
 * Return: 1 if is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *tmp = NULL;

	if (!(*head))
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast)
		slow = slow->next;

	while (slow)
	{
		fast = slow->next;
		slow->next = tmp;
		tmp = slow;
		slow = fast;
	}

	fast = *head;
	while (tmp)
	{
		if (tmp->n != fast->n)
			return (0);
		fast = fast->next;
		tmp = tmp->next;
	}
	return (1);
}

