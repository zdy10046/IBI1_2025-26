import matplotlib.pyplot as plt
gene_expression = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}
print("Gene Expression Dictionary:")
print(gene_expression)
gene_expression["MYC"] = 11.6
print("Gene Expression Dictionary:")
print(gene_expression)
genes = list(gene_expression.keys())
values = list(gene_expression.values())
colors = ['#3498DB' if v > 10 else '#E74C3C' for v in values]#Blue for >10, red for <=10
plt.figure()
plt.bar(genes, values,color=colors)
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")
plt.show()
gene_of_interest = "TP53"
if gene_of_interest in gene_expression:
    print(f"Expression level of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"Error: {gene_of_interest} is not present in the dataset.")

# Calculate average gene expression
average_expression = sum(gene_expression.values()) / len(gene_expression)
print(f"Average gene expression level: {average_expression:.2f}")