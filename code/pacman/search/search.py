<html>
  <head><script src="//archive.org/includes/analytics.js?v=cf34f82" type="text/javascript"></script>
<script type="text/javascript">window.addEventListener('DOMContentLoaded',function(){var v=archive_analytics.values;v.service='wb';v.server_name='wwwb-app19.us.archive.org';v.server_ms=258;archive_analytics.send_pageview({});});</script><script type="text/javascript" src="/static/js/wbhack.js?v=1527197507.0" charset="utf-8"></script>

<script type="text/javascript">
__wbhack.init('https://web.archive.org/web');
</script>
<link rel="stylesheet" type="text/css" href="/static/css/banner-styles.css?v=1527197507.0" />
<link rel="stylesheet" type="text/css" href="/static/css/iconochive.css?v=1527197507.0" />

<!-- End Wayback Rewrite JS Include -->
  <title>search.py</title>
  </head>
  <body>
  <h3>search.py (<a href="http://ai.berkeley.edu/projects/release/search/v1/001/search.zip">original</a>)</h3>
  <hr>
  <pre>
<span style="color: green; font-style: italic"># search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


</span><span style="color: darkred">"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

</span><span style="color: blue; font-weight: bold">import </span>util

<span style="color: blue; font-weight: bold">class </span>SearchProblem<span style="font-weight: bold">:
    </span><span style="color: darkred">"""
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    </span><span style="color: blue; font-weight: bold">def </span>getStartState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Returns the start state for the search problem.
        """
        </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

    </span><span style="color: blue; font-weight: bold">def </span>isGoalState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

    </span><span style="color: blue; font-weight: bold">def </span>getSuccessors<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

    </span><span style="color: blue; font-weight: bold">def </span>getCostOfActions<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>actions<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()


</span><span style="color: blue; font-weight: bold">def </span>tinyMazeSearch<span style="font-weight: bold">(</span>problem<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    </span><span style="color: blue; font-weight: bold">from </span>game <span style="color: blue; font-weight: bold">import </span>Directions
    s <span style="font-weight: bold">= </span>Directions<span style="font-weight: bold">.</span>SOUTH
    w <span style="font-weight: bold">= </span>Directions<span style="font-weight: bold">.</span>WEST
    <span style="color: blue; font-weight: bold">return  </span><span style="font-weight: bold">[</span>s<span style="font-weight: bold">, </span>s<span style="font-weight: bold">, </span>w<span style="font-weight: bold">, </span>s<span style="font-weight: bold">, </span>w<span style="font-weight: bold">, </span>w<span style="font-weight: bold">, </span>s<span style="font-weight: bold">, </span>w<span style="font-weight: bold">]

</span><span style="color: blue; font-weight: bold">def </span>depthFirstSearch<span style="font-weight: bold">(</span>problem<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    </span><span style="color: red">"*** YOUR CODE HERE ***"
    </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

</span><span style="color: blue; font-weight: bold">def </span>breadthFirstSearch<span style="font-weight: bold">(</span>problem<span style="font-weight: bold">):
    </span><span style="color: darkred">"""Search the shallowest nodes in the search tree first."""
    </span><span style="color: red">"*** YOUR CODE HERE ***"
    </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

</span><span style="color: blue; font-weight: bold">def </span>uniformCostSearch<span style="font-weight: bold">(</span>problem<span style="font-weight: bold">):
    </span><span style="color: darkred">"""Search the node of least total cost first."""
    </span><span style="color: red">"*** YOUR CODE HERE ***"
    </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

</span><span style="color: blue; font-weight: bold">def </span>nullHeuristic<span style="font-weight: bold">(</span>state<span style="font-weight: bold">, </span>problem<span style="font-weight: bold">=</span><span style="color: blue">None</span><span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    </span><span style="color: blue; font-weight: bold">return </span><span style="color: red">0

</span><span style="color: blue; font-weight: bold">def </span>aStarSearch<span style="font-weight: bold">(</span>problem<span style="font-weight: bold">, </span>heuristic<span style="font-weight: bold">=</span>nullHeuristic<span style="font-weight: bold">):
    </span><span style="color: darkred">"""Search the node that has the lowest combined cost and heuristic first."""
    </span><span style="color: red">"*** YOUR CODE HERE ***"
    </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()


</span><span style="color: green; font-style: italic"># Abbreviations
</span>bfs <span style="font-weight: bold">= </span>breadthFirstSearch
dfs <span style="font-weight: bold">= </span>depthFirstSearch
astar <span style="font-weight: bold">= </span>aStarSearch
ucs <span style="font-weight: bold">= </span>uniformCostSearch

  </pre>
  </body>
  </html>
  <!--
     FILE ARCHIVED ON 07:39:29 Sep 09, 2016 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 07:21:33 May 28, 2018.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
-->
<!--
playback timings (ms):
  LoadShardBlock: 97.813 (3)
  esindex: 0.007
  captures_list: 118.108
  CDXLines.iter: 15.825 (3)
  PetaboxLoader3.datanode: 102.281 (4)
  exclusion.robots: 0.243
  exclusion.robots.policy: 0.231
  RedisCDXSource: 0.797
  PetaboxLoader3.resolve: 98.035
  load_resource: 121.276
-->
