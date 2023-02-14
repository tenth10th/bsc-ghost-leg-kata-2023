Tara:
    It's important to discuss where we're going...
    Starting with the simplest case doesn't give as much value as discussing the bigger picture
    There's no reason to not discuss, and make sure we're on the same page!
    (Tara's instinct to take notes was great!)

Diana:
    We as talkers need to be better about details like "equals" vs. "double equals" vs. "is equals"
    It's a very good Kata, well laid out in advance
        Gitpod session ready to go
        Document with illustrations and examples
        And a Google Draw canvas to build and "run" Ghost Legs by hand

Andrei:
    When people switch roles, there's a need for discussion
    Does switching off people at regular intervals provide a benefit that justifies the context switch?
    (Better to switch off, say, at the end of a TDD cycle)
    (or to end each "turn" by writing a failing test?)
    A good example of why it's better to have smart data structure than smart code
        Illustrated that maybe legs should be indices rather than strings?

Dave:
    I've done this before, so this is a slightly improved/streamlined version...
        Split up the notes into separate pages:
            What is a ghost leg, how do they work
            How might you implement one?
            Advanced / challenges

    But it was great to do it a new way:
        I learn something every time
        But a lot more when we try a new approach!

    I should have said, "How should this work if we don't pass in the whole array?"
        Instead of just "Fixing it"
        (and by "fixing it", I mean, going off on a tangent that didn't help at all)
        (that took us ~2 cycles to recover from...)

    There's an "extreme programming exercise" that I was reminded of in our discussions around testing and ensemble programming:
        No talking!
        Communicate only by writing failing tests...
        Then letting the next person make a test pass
            And write the next failing test
        It becomes very important to name everything really well, and follow TDD!

Gitpod is pretty good!
If everyone has Desktop VSCode *
    (at the same version!)
    And has the VSCode Live Share extension installed
        (also at the same version!)
    It's slightly better
        You can see everyone's cursor moving around
        And you can "follow" a member of the share
            And everyone's VSCode will switch files
            Open tab, etc.
            To follow what the driver is doing
    Downsides:
        It also fails intermittently
        (And it is more subtle / hard to tell when it fails)
        (and it may fail for one person only!)

Alternately (see Chuba's notes below):
    Everyone can run browser-based VSCode, getting them onto a common version without installing anything locally...

    Then just have to enable VS Code LiveShare

    (Logging into LiveShare can be tricky... But you can do it using GitHub or Microsoft credentials)**

Chuba: 
    * They can use VS Code on their browsers instead of installing, no need for everyone to satisfy all the if-conditions
    ** They can log in as Guests without GitHub or Microsoft accts (though have to be approved by host)
    It is possible to swap elements in Python in one line:

    # Swapping array elements in Python
    list[pos1], list[pos2] = list[pos2], list[pos1]
    https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/

    (next time?)
    We could try modeling the legs as a graph with an adjacency matrix that also stores the order, e.g.:
    {
        A: [B,D]
        ...
    }
    means we swap A with B on the first pass and swap with D the next time.