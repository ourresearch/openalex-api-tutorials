{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cd151571-2976-4e81-a1e2-2cf716466271",
   "metadata": {},
   "source": [
    "<div align=\"center\">\n",
    "    <a href=\"https://openalex.org/\">\n",
    "        <img src=\"../../resources/img/OpenAlex-logo.png\" alt=\"OpenAlex logo\" width=\"300\">\n",
    "    </a>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e141e5ff-f69d-4563-a556-ce1e746aef14",
   "metadata": {},
   "source": [
    "# Monitoring Open Access publications for a given institution\n",
    "\n",
    "<div style='background:#e7edf7'>\n",
    "    In this notebook we will query the OpenAlex API to answer the question:\n",
    "    <blockquote>\n",
    "        <b><i>How many of recent journal articles from a given institution are Open Access? And how many aren't?</i></b>\n",
    "    </blockquote>\n",
    "    To get to the bottom of this, we will use the following API functionalities: \n",
    "    <a href=\"https://docs.openalex.org/api/get-lists-of-entities#filter\">filtering</a> and \n",
    "    <a href=\"https://docs.openalex.org/api/get-groups-of-entities\">grouping</a>\n",
    "</div>\n",
    "<br>\n",
    "\n",
    "Imagine you would like to track the University of Florida's progress in the transition towards Open Access (OA). How could you do that using OpenAlex?\n",
    "\n",
    "\n",
    "Let's start by dividing the process into smaller, more manageable steps:\n",
    "1. First we need to get all recent journal articles from the University of Florida\n",
    "2. Next we divide them into open and closed access\n",
    "3. Finally we count the publications in each category\n",
    "4. Additionally we can put the numbers into a plot to visualize our findings\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7216c04-3575-4d14-a4ed-5bb66401f5e4",
   "metadata": {},
   "source": [
    "## 1. Get all recent journal articles from the University of Florida\n",
    "The first step in querying OpenAlex is always to build the URL to get exactly the data we need. We need to ask two things:\n",
    "1. About which entity type (author, concept, institution, venue, work) do we want data?  \n",
    " --> Since we want to query for metadata about \"_journal articles_\", the entity type should be `works`.\n",
    "\n",
    "2. What are the criteria the works need to fulfill to fit our purpose?  \n",
    "   Here we need to look into the list of available [filters for works](https://docs.openalex.org/api/get-lists-of-entities/filter-entity-lists#works-filters) and select the appropriate ones.  \n",
    " --> We want to query for \"_all recent journal articles from the University of Florida_\", so we will filter for the works that:\n",
    "    * were published in the last 10 years (=recent):  \n",
    "    `from_publication_date:2012-07-31`,\n",
    "    * are specified as journal articles:   \n",
    "    `type:journal-article`,\n",
    "    * have at least one [authorship](https://docs.openalex.org/about-the-data/work#authorships) affiliation with the University of Florida:  \n",
    "   `institutions.ror:https://ror.org/02y3ad647`,\n",
    "    * are not [paratext](https://docs.openalex.org/about-the-data/work#is_paratext):  \n",
    "   `is_paratext:false`\n",
    "\n",
    "Now we need to put the URL together from these parts as follows:  \n",
    "* Starting with the base URL \"`https://api.openalex.org/`\", we add the entity type to it : \"`https://api.openalex.org/works`\"\n",
    "* All criteria need to go into the query parameter `filter` that is added after a question mark: \"`https://api.openalex.org/works?filter=`\"\n",
    "* Finally we take the criteria we specified before and concatenate them using commas as separators. This will be our `filter` value: \"`https://api.openalex.org/works?filter=institutions.ror:https://ror.org/02y3ad647,type:journal-article,from_publication_date:2012-07-31,is_paratext:false`\"\n",
    "\n",
    "With this URL we can get all recent journal articles from the University of Florida!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "98345207-4fa0-4799-ba03-5179491adbda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "filter query parameter:\n",
      "  filter=institutions.ror:https://ror.org/02y3ad647,is_paratext:false,type:journal-article,from_publication_date:2012-07-31\n",
      "complete URL:\n",
      "  https://api.openalex.org/works?filter=institutions.ror:https://ror.org/02y3ad647,is_paratext:false,type:journal-article,from_publication_date:2012-07-31\n"
     ]
    }
   ],
   "source": [
    "# build the 'filter' parameter\n",
    "filter_by_institution_id = 'institutions.ror:https://ror.org/02y3ad647'\n",
    "filter_by_paratext = 'is_paratext:false'\n",
    "filter_by_type = 'type:journal-article'\n",
    "filter_by_publication_date = 'from_publication_date:2012-07-31'\n",
    "\n",
    "all_filters = (filter_by_institution_id, filter_by_paratext, filter_by_type, filter_by_publication_date)\n",
    "filter_param = f'filter={\",\".join(all_filters)}'\n",
    "print(f'filter query parameter:\\n  {filter_param}')\n",
    "\n",
    "# put the URL together\n",
    "filtered_works_url = f'https://api.openalex.org/works?{filter_param}'\n",
    "print(f'complete URL:\\n  {filtered_works_url}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58b725da-3088-4e5b-b69a-2b3c18487956",
   "metadata": {},
   "source": [
    "## 2. Divide them into open and closed access\n",
    "To get the number of open and closed works, we need to find an additional attribute that we can use to divide the retrieved works further into these categories. Fortunately OpenAlex includes information about the access status of a work in its metadata via the nested [OpenAccess object](https://docs.openalex.org/about-the-data/work#the-openaccess-object). It is made up of the three attributes\n",
    "* `is_oa` _(Boolean): True if this work is Open Access._\n",
    "* `oa_status` _(String): The Open Access (OA) status of this work. Possible values are gold, green, hybrid, bronze, closed._\n",
    "* `oa_url` _(String): The best Open Access (OA) URL for this work._\n",
    "\n",
    "**-->`is_oa` seems to be exactly the criterion we are looking for!**\n",
    "\n",
    "\n",
    "#### Shortcut `group_by`\n",
    "So one way to get the number of open and closed works would be to add `is_oa` as an additional filter to our query and query OpenAlex for each value in its range `{true, false}` to get its resulting count of works, e.g.\n",
    "* `filter=...,is_oa:true`\n",
    "* `filter=...,is_oa:false`\n",
    "\n",
    "\n",
    "But wait! Isn't that exactly what `group_by` does?  \n",
    "Yes, absolutely, the `group_by` parameter takes one attribute as input, divides the list of results based on the attribute's values and returns each of their counts. What a time saver!\n",
    "\n",
    "Let's add `group_by=is_oa` as an additional query parameter to the end of our URL:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bc0569ad-cd73-460e-8472-27d92c310ff6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "complete URL with group_by:\n",
      "  https://api.openalex.org/works?filter=institutions.ror:https://ror.org/02y3ad647,is_paratext:false,type:journal-article,from_publication_date:2012-07-31&group_by=is_oa\n"
     ]
    }
   ],
   "source": [
    "group_by_param = 'group_by=is_oa'\n",
    "\n",
    "work_groups_url = f'{filtered_works_url}&{group_by_param}'\n",
    "print(f'complete URL with group_by:\\n  {work_groups_url}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc97ecd0-2605-4702-b48b-c83d9d090a95",
   "metadata": {},
   "source": [
    "## 3. Count the number of works in each group\n",
    "\n",
    "After putting together the URL, we can query OpenAlex for the groups of publications and retrieve the following two groups:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a7768120-47af-4a3a-bfda-f5cd7fed3046",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\n",
      "  {\n",
      "    \"key\": \"true\",\n",
      "    \"key_display_name\": \"true\",\n",
      "    \"count\": 37362\n",
      "  },\n",
      "  {\n",
      "    \"key\": \"false\",\n",
      "    \"key_display_name\": \"false\",\n",
      "    \"count\": 31630\n",
      "  }\n",
      "]\n"
     ]
    }
   ],
   "source": [
    "import requests, json\n",
    "response = requests.get(work_groups_url)\n",
    "work_groups = response.json()['group_by']\n",
    "print(json.dumps(work_groups, indent=2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8dc253db-a7b9-4cc3-93eb-5ab0d20f471f",
   "metadata": {},
   "source": [
    "Each group is made up of its `key` that contains the attribute value for the `group_by` attribute, in our case `is_oa`, and its `count` of entities belonging to the group. Given these data we can already answer our initial question:  \n",
    "> _How many of recent journal articles from a given institution are Open Access? And how many aren't?_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cbe98e13-7716-4967-ac93-a3a7b420c3a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--> The first group includes all works where `is_oa` is true and has a count of 37362 publications.\n",
      "--> The second group includes all works where `is_oa` is false and has a count of 31630 publications.\n",
      "That makes an OA percentage of 54.154105\n"
     ]
    }
   ],
   "source": [
    "from num2words import num2words\n",
    "\n",
    "open_works_count = 0\n",
    "closed_works_count = 0\n",
    "for index, group in enumerate(work_groups):\n",
    "    print(f\"--> The {num2words(index+1, ordinal=True)} group includes all works where `is_oa` is {group['key']} and has a count of {group['count']} publications.\")\n",
    "    \n",
    "    if group['key']==\"true\":\n",
    "        open_works_count += group['count']\n",
    "    else: \n",
    "        closed_works_count += group['count']\n",
    "    \n",
    "total_works_count = open_works_count + closed_works_count\n",
    "print('That makes an OA percentage of %f' % (100 * open_works_count/total_works_count))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ead1c279-ffd5-41bf-bd66-dd1cf9f8b3ce",
   "metadata": {},
   "source": [
    "## 4. Plot the data (optional)\n",
    "Last but not least we can put the data into a visually appealing plot. How about a donut plot?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9b1f4de3-3a74-4a30-98a9-597e27778f96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x396 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "plt.rcParams[\"figure.figsize\"] = (8,5.5)\n",
    "\n",
    "# set labels and their respective values\n",
    "groups = ['Open Access', 'Closed Access']\n",
    "counts = [open_works_count, closed_works_count]\n",
    "  \n",
    "# some visual settings\n",
    "colors = ['#23c552', '#f84f31']\n",
    "explode = (0.01, 0.01)\n",
    "  \n",
    "# pie chart\n",
    "plt.pie(counts, colors=colors, labels=groups,\n",
    "        autopct='%1.1f%%', pctdistance=0.85,\n",
    "        explode=explode, textprops={'fontsize': 14})\n",
    "  \n",
    "# make it a donut (draw circle in the middle)\n",
    "centre_circle = plt.Circle((0, 0), 0.70, fc='white')\n",
    "fig = plt.gcf()\n",
    "fig.gca().add_artist(centre_circle)\n",
    "\n",
    "# display chart\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "403a64ee-56e5-41d6-b472-cd63765f7217",
   "metadata": {},
   "source": [
    "---\n",
    "Feel free to use the notebook and determine the percentage of Open Access works for your institution or tweak the filters to fit your analysis.  \n",
    "\n",
    "Happy exploring! 😎"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
