#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the ptr node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *ptr;

	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
		return (NULL);
	ptr->n = number;

	if (node == NULL || node->n >= number)
	{
		ptr->next = node;
		*head = ptr;
		return (ptr);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	ptr->next = node->next;
	node->next = ptr;

	return (ptr);
}
