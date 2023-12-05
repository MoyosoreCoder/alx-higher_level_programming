#include "lists.h"
/**
 * insert_node - linked list that inserts a node
 * @head: first pointer  pointing to the first node
 * @number: the number in the node to insert
 * Return: the new memory for the new insertion
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new;

	new =  malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	/*assigning value to the new node*/
	new->n = number;
	/*checking how to put the correct number in ascending order*/
	if (current == NULL || current->n >= number)
	{
		new->next = current;
		/*allocating new memory for the new head*/
		*head = new;
		return (new);
	}
	while (current->next && current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;

	return (new);
}
