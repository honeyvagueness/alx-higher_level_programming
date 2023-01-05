#include "lists.h"

/**
 * insert_node - adds a node in a sorted list
 *
 * @head: pointer to the list
 * @n: data to add
 *
 * Return: returns pointer to new node
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new, *tmp, *prev;

	if (!head)
		return (0);
	new = malloc(sizeof(*new));
	if (!new)
		return (0);
	new->n = n;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	tmp = prev = *head;
	while (tmp && tmp->n < n)
	{
		prev = tmp;
		tmp = tmp->next;
	}
	if (prev == tmp)
		*head = new;
	else
		prev->next = new;
	new->next = tmp;
	return (new);
}
